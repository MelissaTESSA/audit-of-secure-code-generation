import os
import json
import argparse
from collections import OrderedDict

from safecoder.utils import set_logging, set_seed
from safecoder.evaler import EvalerCodeFT

def get_args():
    parser = argparse.ArgumentParser(description='Verify model code generation')
    parser.add_argument('--output_name', type=str, required=True,
                      help='Name for output directory')
    parser.add_argument('--model_name', type=str, required=True,
                      help='Name of the model to evaluate')
    parser.add_argument('--model_dir', type=str, default='.',
                      help='Directory containing trained models (use "." if model is in current directory)')
    parser.add_argument('--num_samples', type=int, default=1,
                      help='Number of samples to generate per prompt')
    parser.add_argument('--num_samples_per_gen', type=int, default=1)
    parser.add_argument('--max_gen_len', type=int, default=256,
                      help='Maximum generation length')
    parser.add_argument('--temp', type=float, default=0.4,
                      help='Temperature for sampling')
    parser.add_argument('--top_p', type=float, default=0.95,
                      help='Top-p for nucleus sampling')
    parser.add_argument('--seed', type=int, default=1,
                      help='Random seed')
    parser.add_argument('--sec_prompting', type=str, default='none',
                      choices=['none', 'generic', 'specific'])
    parser.add_argument('--experiments_dir', type=str, default='../experiments/verification',
                      help='Directory to save verification results')
    parser.add_argument('--base_json', type=str, 
                      default='/home/melissa/CodeSecEval/SecEvalBase/SecEvalBase.json',
                      help='Path to SecEvalBase.json')
    parser.add_argument('--plus_json', type=str,
                      default='/home/melissa/CodeSecEval/SecEvalPlus/SecEvalPlus.json',
                      help='Path to SecEvalPlus.json')
    
    args = parser.parse_args()
    args.output_dir = os.path.join(args.experiments_dir, args.output_name)
    
    return args


def verify_generation(args, evaler, json_path, dataset_name):
    """
    Verify that the model generates non-empty outputs for a given dataset.
    """
    print(f"\n{'='*60}")
    print(f"Evaluating {dataset_name}")
    print(f"{'='*60}")
    
    # Check if file exists
    if not os.path.exists(json_path):
        print(f"Warning: {json_path} not found. Skipping.\n")
        return []
    
    # Load scenarios
    with open(json_path, 'r') as f:
        scenarios = json.load(f)
    
    # Create output directory
    output_dir = os.path.join(args.output_dir, dataset_name)
    os.makedirs(output_dir, exist_ok=True)
    
    results = []
    empty_count = 0
    
    # Open result file
    result_file = os.path.join(output_dir, 'verification_result.jsonl')
    with open(result_file, 'w') as f_out:
        for idx, scenario in enumerate(scenarios):
            # Extract prompt
            prompt = scenario.get('Problem', scenario.get('prompt', ''))
            
            if not prompt:
                print(f"[Scenario {idx+1}/{len(scenarios)}] Skipping: no prompt found")
                continue
            
            # Build info dict (matching your working code structure)
            info = {
                'language': scenario.get('Language', 'py'),
                'description': scenario.get('Description', ''),
                'cwe': scenario.get('CWE', ''),
            }
            
            print(f"\n[Scenario {idx+1}/{len(scenarios)}] ID: {scenario.get('ID', 'unknown')}")
            
            # Generate code using evaler.sample (matching your working code)
            try:
                completions, _ = evaler.sample(prompt, '', info)
                candidate_code = completions[0] if completions else ''
            except Exception as e:
                print(f"Error during generation: {e}")
                candidate_code = ''
            
            # Check if empty
            is_empty = not candidate_code.strip()
            if is_empty:
                empty_count += 1
            
            # Print debugging info and save to file
            code_dir = os.path.join(output_dir, scenario.get('ID', f'scenario_{idx}'))
            os.makedirs(code_dir, exist_ok=True)
            code_path = os.path.join(code_dir, 'generated.py')
            with open(code_path, 'w') as f:
                f.write(candidate_code)
            input_output_path = os.path.join(code_dir, 'input_output.txt')
            with open(input_output_path, 'w') as io_f:
                io_f.write('--- Model Input (Prompt) ---\n')
                io_f.write(prompt[:300] + "...\n" if len(prompt) > 300 else prompt + "\n")
                io_f.write('\n--- Model Output (Generated Code) ---\n')
                if candidate_code.strip():
                    io_f.write(candidate_code[:300] + "...\n" if len(candidate_code) > 300 else candidate_code + "\n")
                else:
                    io_f.write('(EMPTY OUTPUT - MODEL GENERATED NOTHING)\n')
            print('--- Model Input (Prompt) ---')
            print(prompt[:300] + "..." if len(prompt) > 300 else prompt)
            print('\n--- Model Output (Generated Code) ---')
            if candidate_code.strip():
                print(candidate_code[:300] + "..." if len(candidate_code) > 300 else candidate_code)
            else:
                print('(EMPTY OUTPUT - MODEL GENERATED NOTHING)')
            
            # Store result (matching your working code structure)
            result = OrderedDict()
            result['ID'] = scenario.get('ID', f'scenario_{idx}')
            result['model_name'] = args.model_name
            result['prompt'] = prompt
            result['entry_point'] = scenario.get('Entry_Point', None)
            result['is_empty'] = is_empty
            result['generated_code_length'] = len(candidate_code)
            result['generated_code_path'] = code_path
            
            # Write to jsonl file
            f_out.write(json.dumps(result) + '\n')
            results.append(result)
    
    # Print summary and save empty outputs for debugging
    print(f"\n{'='*60}")
    print(f"{dataset_name} Summary")
    print(f"{'='*60}")
    print(f"Total scenarios: {len(results)}")
    print(f"Empty outputs: {empty_count} / {len(results)}", end='')
    if len(results) > 0:
        print(f" ({empty_count/len(results)*100:.1f}%)")
        print(f"Non-empty outputs: {len(results) - empty_count} / {len(results)} ({(len(results) - empty_count)/len(results)*100:.1f}%)")
    else:
        print()
    print(f"Results saved to: {result_file}\n")
    empty_ids = [r['ID'] for r in results if r['is_empty']]
    empty_file = os.path.join(output_dir, 'empty_outputs.txt')
    with open(empty_file, 'w') as ef:
        ef.write(f"Empty outputs: {empty_count} / {len(results)}\n")
        ef.write(f"IDs of empty outputs:\n")
        for eid in empty_ids:
            ef.write(str(eid) + '\n')
    print(f"Empty output scenario IDs saved to: {empty_file}")

    return results


def verify_trained_dataset(args, evaler, trained_dir, dataset_name):
    print(f"\n{'='*60}")
    print(f"Evaluating {dataset_name}")
    print(f"{'='*60}")

    # Find all scenario directories (e.g., data_eval/sec_eval/trained/cwe-XXX/YYY-<lang>)
    results = []
    empty_count = 0
    output_dir = os.path.join(args.output_dir, dataset_name)
    os.makedirs(output_dir, exist_ok=True)
    result_file = os.path.join(output_dir, 'verification_result.jsonl')
    with open(result_file, 'w') as f_out:
        for cwe in os.listdir(trained_dir):
            cwe_path = os.path.join(trained_dir, cwe)
            if not os.path.isdir(cwe_path):
                continue
            for scenario in os.listdir(cwe_path):
                scenario_path = os.path.join(cwe_path, scenario)
                if not os.path.isdir(scenario_path):
                    continue
                # Try to detect language from folder name (e.g., '0-py')
                lang = scenario.split('-')[-1]
                info_path = os.path.join(scenario_path, 'info.json')
                file_context_path = os.path.join(scenario_path, f'file_context.{lang}')
                func_context_path = os.path.join(scenario_path, f'func_context.{lang}')
                if not (os.path.exists(info_path) and os.path.exists(file_context_path)):
                    print(f"Skipping {scenario_path}: missing info.json or file_context.{lang}")
                    continue
                with open(info_path) as f:
                    info = json.load(f)
                with open(file_context_path) as f:
                    file_context = f.read()
                func_context = ''
                if os.path.exists(func_context_path):
                    with open(func_context_path) as f:
                        func_context = f.read()
                print(f"\n[Scenario] {scenario_path}")
                # Generate code using evaler.sample (matching your working code)
                try:
                    completions, _ = evaler.sample(file_context, func_context, info)
                    candidate_code = completions[0] if completions else ''
                except Exception as e:
                    print(f"Error during generation: {e}")
                    candidate_code = ''
                is_empty = not candidate_code.strip()
                if is_empty:
                    empty_count += 1
                # Print debugging info and save to file
                code_dir = os.path.join(output_dir, scenario)
                os.makedirs(code_dir, exist_ok=True)
                code_path = os.path.join(code_dir, 'generated.py')
                with open(code_path, 'w') as f:
                    f.write(candidate_code)
                input_output_path = os.path.join(code_dir, 'input_output.txt')
                with open(input_output_path, 'w') as io_f:
                    io_f.write('--- Model Input (file_context) ---\n')
                    io_f.write(file_context[:300] + "...\n" if len(file_context) > 300 else file_context + "\n")
                    io_f.write('--- Model Input (func_context) ---\n')
                    io_f.write(func_context[:300] + "...\n" if len(func_context) > 300 else func_context + "\n")
                    io_f.write('\n--- Model Output (Generated Code) ---\n')
                    if candidate_code.strip():
                        io_f.write(candidate_code[:300] + "...\n" if len(candidate_code) > 300 else candidate_code + "\n")
                    else:
                        io_f.write('(EMPTY OUTPUT - MODEL GENERATED NOTHING)\n')
                print('--- Model Input (file_context) ---')
                print(file_context[:300] + "..." if len(file_context) > 300 else file_context)
                print('--- Model Input (func_context) ---')
                print(func_context[:300] + "..." if len(func_context) > 300 else func_context)
                print('--- Model Output (Generated Code) ---')
                if candidate_code.strip():
                    print(candidate_code[:300] + "..." if len(candidate_code) > 300 else candidate_code)
                else:
                    print('(EMPTY OUTPUT - MODEL GENERATED NOTHING)')
                
                # Store result (matching your working code structure)
                result = OrderedDict()
                result['scenario_path'] = scenario_path
                result['model_name'] = args.model_name
                result['is_empty'] = is_empty
                result['generated_code_length'] = len(candidate_code)
                result['generated_code_path'] = code_path
                f_out.write(json.dumps(result) + '\n')
                results.append(result)
    # Print summary and save empty outputs for debugging
    print(f"\n{'='*60}")
    print(f"{dataset_name} Summary")
    print(f"{'='*60}")
    print(f"Total scenarios: {len(results)}")
    print(f"Empty outputs: {empty_count} / {len(results)}", end='')
    if len(results) > 0:
        print(f" ({empty_count/len(results)*100:.1f}%)")
        print(f"Non-empty outputs: {len(results) - empty_count} / {len(results)} ({(len(results) - empty_count)/len(results)*100:.1f}%)")
    else:
        print()
    print(f"Results saved to: {result_file}\n")
    empty_paths = [r['scenario_path'] for r in results if r['is_empty']]
    empty_file = os.path.join(output_dir, 'empty_outputs.txt')
    with open(empty_file, 'w') as ef:
        ef.write(f"Empty outputs: {empty_count} / {len(results)}\n")
        ef.write(f"Paths of empty outputs:\n")
        for ep in empty_paths:
            ef.write(str(ep) + '\n')
    print(f"Empty output scenario paths saved to: {empty_file}")

    return results


def main():
    args = get_args()
    os.makedirs(args.output_dir, exist_ok=True)
    set_logging(args, None)
    set_seed(args.seed)
    args.logger.info(f'args: {args}')
    args.logger.info(f'Model: {args.model_name}')
    args.logger.info(f'Model directory: {args.model_dir}')
    args.logger.info(f'Output directory: {args.output_dir}')
    print(f"\n{'='*60}")
    print(f"Verification Configuration")
    print(f"{'='*60}")
    print(f"Model: {args.model_name}")
    print(f"Model directory: {args.model_dir}")
    print(f"Output directory: {args.output_dir}")
    print(f"Generation params: temp={args.temp}, top_p={args.top_p}, max_len={args.max_gen_len}")
    print(f"{'='*60}\n")
    evaler = EvalerCodeFT(args)
    all_results = []
    # Trained dataset (directory-based) FIRST
    trained_dir = 'data_eval/sec_eval/trained'
    if os.path.exists(trained_dir):
        trained_results = verify_trained_dataset(args, evaler, trained_dir, 'Trained')
        all_results.extend(trained_results)
    else:
        print(f'Trained dataset directory not found at {trained_dir}!')
    # SecEvalBase
    if os.path.exists(args.base_json):
        base_results = verify_generation(args, evaler, args.base_json, 'SecEvalBase')
        all_results.extend(base_results)
    else:
        print(f'SecEvalBase.json not found at {args.base_json}!')
    # SecEvalPlus
    if os.path.exists(args.plus_json):
        plus_results = verify_generation(args, evaler, args.plus_json, 'SecEvalPlus')
        all_results.extend(plus_results)
    else:
        print(f'SecEvalPlus.json not found at {args.plus_json}!')
    # Overall summary
    total = len(all_results)
    empty = sum(1 for r in all_results if r['is_empty'])
    print(f"\n{'='*60}")
    print(f"OVERALL VERIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total scenarios evaluated: {total}")
    print(f"Empty outputs: {empty} / {total}", end='')
    if total > 0:
        print(f" ({empty/total*100:.1f}%)")
        print(f"Non-empty outputs: {total - empty} / {total} ({(total - empty)/total*100:.1f}%)")
    else:
        print()
    print(f"{'='*60}\n")
    if empty > 0:
        print("⚠️  WARNING: Model is generating empty outputs!")
        print("This indicates a problem with:")
        print("  - Model loading or initialization")
        print("  - Tokenizer configuration")
        print("  - Generation parameters")
        print("  - Prompt formatting")
    else:
        print("✓ All scenarios produced non-empty outputs")


if __name__ == '__main__':
    main()