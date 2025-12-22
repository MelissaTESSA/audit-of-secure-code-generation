import os
import subprocess
import sys
import glob
import csv

# Usage: python codeql_analysis.py <scenarios_dir> [language] [queries_root]

def run_codeql_analysis(scenarios_dir, language='python', queries_root=None):
    if queries_root is None:
        queries_root = os.path.expanduser('~/.codeql/packages/codeql/python-queries/0.9.0/Security')
    
    print("\n" + "="*80)
    print("STARTING CODEQL ANALYSIS")
    print("="*80)
    print(f"Scenarios directory: {scenarios_dir}")
    print(f"Language: {language}")
    print(f"Queries root: {queries_root}")
    print(f"=" * 80 + "\n")
    sys.stdout.flush()
    
    summary = []
    
    scenarios = sorted(os.listdir(scenarios_dir))
    total_scenarios = len([s for s in scenarios if os.path.isdir(os.path.join(scenarios_dir, s)) and s.startswith('CWE-')])
    
    print(f"Found {total_scenarios} scenarios to process\n")
    sys.stdout.flush()
    
    scenario_counter = 0
    
    for scenario in scenarios:
        scenario_path = os.path.join(scenarios_dir, scenario)
        if not os.path.isdir(scenario_path):
            continue
        
        # Extract CWE ID
        cwe_id = scenario.split('_')[0] if scenario.startswith('CWE-') else None
        if not cwe_id:
            continue
        
        scenario_counter += 1
        
        print("\n" + "="*80)
        print(f"SCENARIO {scenario_counter}/{total_scenarios}: {scenario}")
        print("="*80)
        sys.stdout.flush()
        
        print(f"CWE ID: {cwe_id}")
        
        # Find code files
        print("Step 1: Looking for code files...")
        sys.stdout.flush()
        
        if language == 'python':
            code_files = [f for f in os.listdir(scenario_path) if f.endswith('.py')]
        elif language in ('c', 'cpp'):
            code_files = [f for f in os.listdir(scenario_path) if f.endswith(('.c', '.cpp', '.h'))]
        else:
            code_files = [f for f in os.listdir(scenario_path) if not f.startswith('.')]
        
        num_files = len(code_files)
        print(f"  Found {num_files} code files")
        if num_files > 0:
            if num_files <= 10:
                for cf in code_files:
                    print(f"    - {cf}")
            else:
                for cf in code_files[:5]:
                    print(f"    - {cf}")
                print(f"    ... and {num_files - 5} more files")
        sys.stdout.flush()
        
        if num_files == 0:
            print("⚠️  No code files found - skipping\n")
            sys.stdout.flush()
            summary.append({
                'scenario': scenario,
                'cwe': cwe_id,
                'num_files': 0,
                'secure': 0,
                'insecure': 0,
                'avg_secure': 0.0,
                'avg_per_10': 0.0
            })
            continue
        
        # Find all .ql queries for this CWE
        print(f"\nStep 2: Looking for CodeQL queries for {cwe_id}...")
        cwe_query_dir = os.path.join(queries_root, cwe_id)
        print(f"  Query directory: {cwe_query_dir}")
        sys.stdout.flush()
        
        if not os.path.exists(cwe_query_dir):
            print(f"  ⚠️  Query directory does not exist")
            sys.stdout.flush()
            ql_files = []
        else:
            ql_files = glob.glob(os.path.join(cwe_query_dir, '*.ql'))
            if ql_files:
                print(f"  Found {len(ql_files)} query file(s):")
                for ql in ql_files:
                    print(f"    - {os.path.basename(ql)}")
            else:
                print("  No .ql files found in query directory")
            sys.stdout.flush()
        
        if not ql_files:
            print(f"  ⚠️  No queries available for {cwe_id} - assuming all files are secure\n")
            sys.stdout.flush()
            summary.append({
                'scenario': scenario,
                'cwe': cwe_id,
                'num_files': num_files,
                'secure': num_files,
                'insecure': 0,
                'avg_secure': 1.0,
                'avg_per_10': num_files/10.0
            })
            continue
        
        # Create CodeQL database
        print("\nStep 3: Creating CodeQL database...")
        db_dir = os.path.join(scenario_path, 'codeql_db')
        print(f"  Database directory: {db_dir}")
        cmd_create = f'codeql database create {db_dir} --language={language} --overwrite --source-root {scenario_path}'
        print(f"  Running: {cmd_create}")
        sys.stdout.flush()
        
        result = subprocess.run(cmd_create, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"  ❌ Database creation FAILED")
            print(f"  Return code: {result.returncode}")
            if result.stderr:
                print(f"  Error output:\n{result.stderr}")
            sys.stdout.flush()
            continue
        else:
            print(f"  ✓ Database created successfully")
            sys.stdout.flush()
        
        # Finalize database
        print("\nStep 4: Finalizing database...")
        cmd_finalize = f'codeql database finalize {db_dir}'
        print(f"  Running: {cmd_finalize}")
        sys.stdout.flush()
        
        result = subprocess.run(cmd_finalize, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"  ❌ Database finalization FAILED")
            if result.stderr:
                print(f"  Error output:\n{result.stderr}")
        else:
            print(f"  ✓ Database finalized")
        sys.stdout.flush()
        
        # Run each query and collect results
        insecure_files = set()
        
        print(f"\nStep 5: Running {len(ql_files)} quer{'y' if len(ql_files)==1 else 'ies'}...")
        sys.stdout.flush()
        
        for query_idx, ql_file in enumerate(ql_files, 1):
            query_name = os.path.basename(ql_file)
            
            print(f"\n  Query {query_idx}/{len(ql_files)}: {query_name}")
            sys.stdout.flush()
            
            csv_path = os.path.join(scenario_path, f'codeql_results_{query_name}.csv')
            cmd_analyze = f'codeql database analyze {db_dir} {ql_file} --format=csv --output={csv_path}'
            print(f"  Running: {cmd_analyze}")
            sys.stdout.flush()
            
            result = subprocess.run(cmd_analyze, shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"    ❌ Query execution FAILED")
                print(f"    Return code: {result.returncode}")
                if result.stderr:
                    print(f"    Error output:\n{result.stderr}")
                sys.stdout.flush()
                continue
            else:
                print(f"    ✓ Query executed successfully")
                sys.stdout.flush()
            
            # Parse CSV for results
            print(f"    Parsing results from: {csv_path}")
            sys.stdout.flush()
            
            if not os.path.exists(csv_path):
                print(f"    ⚠️  CSV file not created")
                sys.stdout.flush()
                continue
            
            with open(csv_path, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
                
                file_size = os.path.getsize(csv_path)
                print(f"    CSV file: {len(rows)} rows, {file_size} bytes")
                sys.stdout.flush()
                
                if len(rows) <= 1:
                    print(f"    ✓ No vulnerabilities found by this query")
                    sys.stdout.flush()
                    continue
                
                # Print header to understand CSV structure
                if rows and len(rows[0]) > 0:
                    print(f"    CSV columns: {len(rows[0])}")
                    print(f"    CSV header (first 5 columns): {', '.join(rows[0][:5])}")
                    sys.stdout.flush()
                
                # Parse results (skip header)
                vulnerabilities_found = 0
                print(f"    Analyzing {len(rows)-1} result row(s)...")
                sys.stdout.flush()
                
                for i, row in enumerate(rows[1:], 1):
                    if not row or len(row) < 5:
                        print(f"      Row {i}: Skipping (too few columns: {len(row)})")
                        sys.stdout.flush()
                        continue
                    
                    # CodeQL CSV format typically has columns like:
                    # "Name", "Description", "Severity", "Message", "Path", "Start line", "Start column", "End line", "End column"
                    # The file path is usually in column index 4 (0-indexed)
                    
                    file_path = row[4] if len(row) > 4 else row[0]
                    file_path = file_path.strip('"')
                    filename = os.path.basename(file_path)
                    
                    vulnerabilities_found += 1
                    
                    if vulnerabilities_found <= 3:  # Only print first 3 to avoid spam
                        print(f"      Vulnerability {vulnerabilities_found}:")
                        print(f"        File path: {file_path}")
                        print(f"        Filename: {filename}")
                        if len(row) > 3:
                            print(f"        Message: {row[3][:100]}...")
                        sys.stdout.flush()
                    
                    # Check if this file exists in our code files
                    matched = False
                    if filename in code_files:
                        insecure_files.add(filename)
                        matched = True
                        if vulnerabilities_found <= 3:
                            print(f"        ✓ Matched to code file: {filename}")
                            sys.stdout.flush()
                    else:
                        # Try alternative matching
                        for cf in code_files:
                            if cf in file_path or file_path.endswith(cf):
                                insecure_files.add(cf)
                                matched = True
                                if vulnerabilities_found <= 3:
                                    print(f"        ✓ Alternative match: {cf}")
                                    sys.stdout.flush()
                                break
                    
                    if not matched and vulnerabilities_found <= 3:
                        print(f"        ⚠️  Could not match to any code file")
                        print(f"        Available files: {code_files[:3]}...")
                        sys.stdout.flush()
                
                if vulnerabilities_found > 3:
                    print(f"      ... and {vulnerabilities_found - 3} more vulnerabilities")
                    sys.stdout.flush()
                
                if vulnerabilities_found > 0:
                    print(f"    Summary: Found {vulnerabilities_found} vulnerability instance(s)")
                    print(f"    Unique files affected: {len(insecure_files)}")
                    sys.stdout.flush()
        
        num_insecure = len(insecure_files)
        num_secure = num_files - num_insecure
        avg_secure = num_secure / num_files if num_files else 0.0
        avg_per_10 = num_secure / 10.0
        
        print("\n" + "="*60)
        print(f"RESULTS FOR {scenario}:")
        print(f"  Total files:    {num_files}")
        print(f"  Secure files:   {num_secure} ({avg_secure*100:.1f}%)")
        print(f"  Insecure files: {num_insecure} ({(1-avg_secure)*100:.1f}%)")
        if insecure_files:
            print(f"  Insecure file list:")
            for inf in sorted(insecure_files):
                print(f"    - {inf}")
        print("="*60)
        sys.stdout.flush()
        
        summary.append({
            'scenario': scenario,
            'cwe': cwe_id,
            'num_files': num_files,
            'secure': num_secure,
            'insecure': num_insecure,
            'avg_secure': avg_secure,
            'avg_per_10': avg_per_10
        })
    
    # Print final summary
    print('\n' + '='*80)
    print("FINAL SUMMARY")
    print('='*80 + "\n")
    
    total_files = 0
    total_secure = 0
    total_insecure = 0
    total_scenarios = len(summary)
    total_pct_per_10 = 0.0
    
    for s in summary:
        sec_pct = f"({s['avg_secure']*100:.0f}%)"
        pct_per_10 = s['secure'] / 10.0 if s['num_files'] else 0.0
        total_pct_per_10 += pct_per_10
        print(f"{s['scenario']:30} | CWE: {s['cwe']:8} | Files: {s['num_files']:3} | "
              f"Secure: {s['secure']:3} | Insecure: {s['insecure']:3} {sec_pct:6} | "
              f"% secure/10: {pct_per_10:.2f}")
        total_files += s['num_files']
        total_secure += s['secure']
        total_insecure += s['insecure']
    
    print('='*80)
    overall_pct = (total_secure/total_files*100) if total_files else 0
    overall_pct_per_10 = (total_secure/(total_scenarios*10)*100) if total_scenarios else 0
    print(f"{'TOTALS':30} | {'':8}   | Files: {total_files:3} | "
          f"Secure: {total_secure:3} | Insecure: {total_insecure:3} | "
          f"Overall: {overall_pct:.1f}% | Overall % secure/10 (all scenarios): {overall_pct_per_10:.2f}%")
    print('='*80)
    
    print("\n✓ ANALYSIS COMPLETE\n")
    sys.stdout.flush()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python codeql_analysis.py <scenarios_dir> [language] [queries_root]')
        sys.exit(1)
    
    scenarios_dir = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) > 2 else 'python'
    queries_root = sys.argv[3] if len(sys.argv) > 3 else None
    
    run_codeql_analysis(scenarios_dir, language, queries_root)
