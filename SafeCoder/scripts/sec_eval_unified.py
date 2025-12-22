import os
import csv
import json
import shutil
import argparse
import subprocess
import libcst as cst
from libcst.metadata import PositionProvider
from libcst._position import CodePosition
from collections import OrderedDict
import sys
import traceback

from safecoder.utils import set_logging, set_seed, get_cp_args
from safecoder.constants import PRETRAINED_MODELS, CHAT_MODELS, CWES_TRAINED, NEW_EVALS, NOT_TRAINED
from safecoder.evaler import EvalerCodePLM, EvalerCodeFT, EvalerOpenAI, EvalerChat

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_name', type=str, required=True)
    parser.add_argument('--model_name', type=str, default=None)
    parser.add_argument('--eval_type', type=str, choices=['trained', 'trained-new', 'not-trained'], default='trained')
    parser.add_argument('--sec_prompting', type=str, choices=['none', 'generic', 'specific'], default='none')
    parser.add_argument('--vul_type', type=str, default=None)
    parser.add_argument('--num_samples', type=int, default=10)  # Number of completions per scenario
    parser.add_argument('--num_samples_per_gen', type=int, default=10)
    parser.add_argument('--temp', type=float, default=0.4)
    parser.add_argument('--max_gen_len', type=int, default=256)
    parser.add_argument('--top_p', type=float, default=0.95)
    parser.add_argument('--experiments_dir', type=str, default='../experiments/sec_eval')
    parser.add_argument('--data_dir', type=str, default='../data_eval/sec_eval')
    parser.add_argument('--model_dir', type=str, default='../trained')
    parser.add_argument('--codesec_json', type=str, default='../../CodeSecEval/SecEvalBase/SecEvalBase.json')
    parser.add_argument('--seed', type=int, default=1)
    args = parser.parse_args()
    args.output_dir = os.path.join(args.experiments_dir, args.output_name, args.eval_type)
    return args

# Helper to run the test code and capture result
def run_test(candidate_code, test_code, entry_point):
    """
    Execute candidate code and run tests in a proper module context.
    Provides __name__ and __file__ to support Flask and other frameworks.
    """
    local_env = {
        '__name__': '__main__',
        '__file__': '/tmp/test_module.py',
    }
    
    try:
        # Execute the candidate code with proper module context
        exec(candidate_code, local_env)
        
        # Patch candidate function/class name to 'candidate' for test
        if entry_point in local_env:
            local_env['candidate'] = local_env[entry_point]
        else:
            return {'test_passed': False, 'error': f'Entry point {entry_point} not found in generated code.'}
        
        # Run the test code
        exec(test_code, local_env)
        return {'test_passed': True, 'error': None}
    except Exception as e:
        return {'test_passed': False, 'error': traceback.format_exc()}


def eval_codesec_scenario(args, evaler, scenario):
    output_dir = os.path.join(args.output_dir, scenario.get('ID', 'unknown'))
    os.makedirs(output_dir, exist_ok=True)
    # Use Problem field as prompt
    prompt = scenario.get('Problem', '')
    entry_point = scenario.get('Entry_Point', None)
    test_code = scenario.get('Test', None)
    # Build info dict from scenario fields
    info = {
        'language': scenario.get('Language', 'py'),
        'description': scenario.get('Description', ''),
        'cwe': scenario.get('CWE', ''),
        # add other fields if needed
    }
    # Old code for reference:
    # completions, _ = evaler.sample(prompt, '', {})
    completions, _ = evaler.sample(prompt, '', info)
    candidate_code = completions[0] if completions else ''
    # Print model input and output for debugging
    print("\n--- Model Input (Prompt) ---\n")
    print(prompt)
    print("\n--- Model Output (Generated Code) ---\n")
    print(candidate_code)
    # Save generated code
    code_path = os.path.join(output_dir, 'generated.py')
    with open(code_path, 'w') as f:
        f.write(candidate_code)
    # Run test if possible
    test_result = None
    if candidate_code and test_code and entry_point:
        test_result = run_test(candidate_code, test_code, entry_point)
    else:
        test_result = {'test_passed': False, 'error': 'Missing candidate code, test code, or entry point.'}
    # Log result
    result = OrderedDict()
    result['ID'] = scenario.get('ID', 'unknown')
    result['model_name'] = args.model_name
    result['prompt'] = prompt
    result['entry_point'] = entry_point
    result['test_passed'] = test_result['test_passed']
    result['error'] = test_result['error']
    result['generated_code_path'] = code_path
    return result


def eval_codesec_all(args, evaler, json_path, dataset_name):
    print(f"\n=== Evaluating {dataset_name} ===")
    with open(json_path, 'r') as f:
        scenarios = json.load(f)
    output_dir = os.path.join(args.output_dir, dataset_name)
    os.makedirs(output_dir, exist_ok=True)
    results = []
    with open(os.path.join(output_dir, 'result.jsonl'), 'w') as f_out:
        for idx, scenario in enumerate(scenarios):
            if 'Problem' in scenario and 'Test' in scenario and 'Entry_Point' in scenario:
                print(f"\n[Scenario {idx+1}/{len(scenarios)}] ID: {scenario.get('ID', 'unknown')}")
                d = eval_codesec_scenario(args, evaler, scenario)
                print(f"Test passed: {d['test_passed']}, Error: {d['error']}")
                s = json.dumps(d)
                f_out.write(s + '\n')
                results.append(d)
            else:
                print(f"Skipping scenario {idx+1}: missing required fields.")
    return results

def print_dataset_summary(results, dataset_name):
    total = len(results)
    empty_outputs = sum(1 for r in results if not open(r['generated_code_path']).read().strip())
    passed = sum(1 for r in results if r['test_passed'])
    print(f"\n=== {dataset_name} Summary ===")
    print(f"Total scenarios: {total}")
    print(f"Empty outputs: {empty_outputs} / {total} ({empty_outputs/total*100:.1f}%)")
    print(f"Passed tests: {passed} / {total} ({passed/total*100:.1f}%)")
    if total > 0:
        print(f"Pass rate: {passed/total*100:.2f}% (including empty outputs)")


def eval_codesec_scenario_k(args, evaler, scenario, max_k=10):
    output_dir = os.path.join(args.output_dir, scenario.get('ID', 'unknown'))
    os.makedirs(output_dir, exist_ok=True)
    prompt = scenario.get('Problem', '')
    entry_point = scenario.get('Entry_Point', None)
    test_code = scenario.get('Test', None)
    info = {
        'language': scenario.get('Language', 'py'),
        'description': scenario.get('Description', ''),
        'cwe': scenario.get('CWE', ''),
    }
    completions, _ = evaler.sample(prompt, '', info)
    completions = completions[:max_k]
    pass_results = []
    non_empty = False
    print("\n--- Model Input (Prompt) ---\n")
    print(prompt)
    print("\n--- Model Outputs (Generated Codes) ---\n")
    for idx, candidate_code in enumerate(completions):
        code_path = os.path.join(output_dir, f'generated_{idx+1}.py')
        with open(code_path, 'w') as f:
            f.write(candidate_code)
        print(f"Output {idx+1}:")
        print(candidate_code)
        if candidate_code.strip():
            non_empty = True
        if candidate_code and test_code and entry_point:
            test_result = run_test(candidate_code, test_code, entry_point)
        else:
            test_result = {'test_passed': False, 'error': 'Missing candidate code, test code, or entry point.'}
        pass_results.append(test_result['test_passed'])
    return pass_results, completions, non_empty


def eval_codesec_all_k(args, evaler, json_path, dataset_name, k_list):
    print(f"\n=== Evaluating {dataset_name} ===")
    with open(json_path, 'r') as f:
        scenarios = json.load(f)
    output_dir = os.path.join(args.output_dir, dataset_name)
    os.makedirs(output_dir, exist_ok=True)
    all_pass_results = []
    non_empty_count = 0
    passed_count = 0
    for idx, scenario in enumerate(scenarios):
        if 'Problem' in scenario and 'Test' in scenario and 'Entry_Point' in scenario:
            print(f"\n[Scenario {idx+1}/{len(scenarios)}] ID: {scenario.get('ID', 'unknown')}")
            pass_results, completions, non_empty = eval_codesec_scenario_k(args, evaler, scenario, max_k=max(k_list))
            all_pass_results.append(pass_results)
            if non_empty:
                non_empty_count += 1
            if any(pass_results):
                passed_count += 1
        else:
            print(f"Skipping scenario {idx+1}: missing required fields.")
    # Compute pass@K for each K
    total = len(all_pass_results)
    pass_at_k = {}
    for k in k_list:
        passed = sum(1 for pr in all_pass_results if any(pr[:k]))
        pass_at_k[k] = passed / total if total > 0 else 0.0
    # Print summary for dataset
    max_k = max(k_list)
    print(f"\n=== {dataset_name} Custom Summary (k={max_k}) ===")
    print(f"Total scenarios: {total}")
    print(f"Non-empty outputs (at least one of k={max_k}): {non_empty_count} / {total} ({(non_empty_count/total*100 if total else 0):.1f}%)")
    print(f"Passed tests (at least one of k={max_k}): {passed_count} / {total} ({(passed_count/total*100 if total else 0):.1f}%)")
    print(f"Pass rate (at least one of k={max_k} passes): {(passed_count/total*100 if total else 0):.2f}%")
    print(f"\n--- pass@K Results ---")
    for k in k_list:
        print(f"pass@{k}: {pass_at_k[k]*100:.2f}%")
    return pass_at_k, total


def main():
    args = get_args()
    os.makedirs(args.output_dir, exist_ok=True)
    set_logging(args, None)
    set_seed(args.seed)
    args.logger.info(f'args: {args}')
    evaler = EvalerCodeFT(args)
    k_list = [1, 3, 5, 7, 10]
    # Only use the JSON file specified by --codesec_json
    if os.path.exists(args.codesec_json):
        pass_at_k, total = eval_codesec_all_k(args, evaler, args.codesec_json, 'SecEvalPlus', k_list)
        print_pass_at_k_summary(pass_at_k, total, 'SecEvalPlus')
    else:
        print(f'{args.codesec_json} not found!')

if __name__ == '__main__':
    main()
