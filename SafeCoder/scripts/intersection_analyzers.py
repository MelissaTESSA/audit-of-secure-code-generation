"""
intersection_analyzers.py

Aggregates results from multiple security analyzers and marks files as:
- 'vulnerable' if ALL analyzers mark as vulnerable
- 'secure' if ALL analyzers mark as secure
- 'mixed' otherwise

Analyzers: sec_eval_unified.py, codeql_analysis.py, bandit_analysis.py, qwen_analysis.py, gpt4o_analysis.py

Usage:
    python intersection_analyzers.py --inputs sec_eval.txt codeql.txt bandit.txt qwen.txt gpt4o.txt --output intersection_results.txt
"""
import argparse
from collections import defaultdict

# Verdict mapping: 1 = vulnerable, 0 = secure
ANALYZER_NAMES = [
    'sec_eval_unified',
    'codeql_analysis',
    'bandit_analysis',
    'qwen_analysis',
    'gpt4o_analysis',
]

def parse_analyzer_output(filepath):
    """Parse analyzer output and return {filename: verdict} dict."""
    verdicts = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Example line: generated_3.py: 1
            if ':' in line:
                parts = line.split(':', 1)
                fname = parts[0].strip()
                verdict = parts[1].strip().split()[0]
                if verdict in {'0', '1'}:
                    verdicts[fname] = int(verdict)
    return verdicts

def main():
    parser = argparse.ArgumentParser(description='Intersection of analyzer results.')
    parser.add_argument('--inputs', nargs=5, required=True, help='Paths to analyzer outputs (in order: sec_eval, codeql, bandit, qwen, gpt4o)')
    parser.add_argument('--output', required=True, help='Path to output file')
    args = parser.parse_args()

    # Parse all analyzer outputs
    all_results = []
    for path in args.inputs:
        all_results.append(parse_analyzer_output(path))

    # Collect all filenames
    all_files = set()
    for res in all_results:
        all_files.update(res.keys())

    # Aggregate verdicts
    intersection = {}
    for fname in sorted(all_files):
        verdicts = [res.get(fname, None) for res in all_results]
        if None in verdicts:
            intersection[fname] = 'unknown'  # Missing result from one or more analyzers
        elif any(v == 1 for v in verdicts):
            intersection[fname] = 'vulnerable'
        elif all(v == 0 for v in verdicts):
            intersection[fname] = 'secure'
        else:
            intersection[fname] = 'unknown'  # Should not occur, but fallback

    # Write output
    with open(args.output, 'w') as out:
        out.write('File	IntersectionVerdict\n')
        for fname, verdict in intersection.items():
            out.write(f'{fname}\t{verdict}\n')

if __name__ == '__main__':
    main()
