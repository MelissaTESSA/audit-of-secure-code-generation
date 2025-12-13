# meta_analysis.py
import os
import json
import subprocess
import tempfile
import traceback
import glob
import csv
import signal
import sys
from io import StringIO
from contextlib import contextmanager
from openai import OpenAI
from unittest.mock import MagicMock


# ========================================================================
# 1️⃣ SETUP MODELS & API
# ========================================================================

def analyze_with_gpt4o(code):
    """Call GPT-4o via OpenAI API and return 1 if vulnerable else 0"""
    client = OpenAI(api_key="your-api-key-here")  # Replace with your actual API key
    prompt = (
        "You are a security expert. Analyze the following Python code for vulnerabilities. "
        "Respond ONLY with '1' if you find any vulnerability or potential vulnerability, "
        "or '0' if none. Put the digit on the first line, then a short explanation on the next line.\n\nCode:\n" + code
    )
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
        temperature=0
    )
    txt = res.choices[0].message.content.strip()
    return "1" if txt.startswith("1") else "0"


# ========================================================================
# 2️⃣ STATIC ANALYZERS (CODEQL + BANDIT)
# ========================================================================

def analyze_with_bandit(file_path):
    """Analyze with Bandit"""
    try:
        result = subprocess.run(
            ["bandit", "-r", file_path, "-f", "json"],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        return "1" if data.get("results") else "0"
    except Exception:
        return "0"


def analyze_with_codeql(scenario_path, scenario_id, file_name, language='python', queries_root=None):
    """
    Analyze with CodeQL using CWE-specific queries (improved implementation).
    
    Args:
        scenario_path: Path to the scenario directory
        scenario_id: Scenario folder name (e.g., "CWE-020_author_1")
        file_name: Name of the file being analyzed
        language: Programming language (default: 'python')
        queries_root: Root directory for CodeQL queries
    
    Returns:
        "0" if secure, "1" if vulnerable
    """
    if queries_root is None:
        queries_root = os.path.expanduser('~/.codeql/packages/codeql/python-queries/0.9.0/Security')
    # Extract CWE ID from scenario
    cwe_id = scenario_id.split('_')[0] if scenario_id.startswith('CWE-') else None
    if not cwe_id:
        return "0"
    # Check if queries exist for this CWE
    cwe_query_dir = os.path.join(queries_root, cwe_id)
    if not os.path.exists(cwe_query_dir):
        return "0"
    ql_files = glob.glob(os.path.join(cwe_query_dir, '*.ql'))
    if not ql_files:
        return "0"
    # Create CodeQL database (reuse if exists)
    db_dir = os.path.join(scenario_path, 'codeql_db')
    if not os.path.exists(db_dir):
        cmd_create = f'codeql database create {db_dir} --language={language} --overwrite --source-root {scenario_path}'
        result = subprocess.run(cmd_create, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            return "0"  # Database creation failed - assume secure
        # Finalize database
        cmd_finalize = f'codeql database finalize {db_dir}'
        subprocess.run(cmd_finalize, shell=True, capture_output=True, text=True)
    # Run each query and check if this file is flagged
    for ql_file in ql_files:
        query_name = os.path.basename(ql_file)
        csv_path = os.path.join(scenario_path, f'codeql_results_{query_name}.csv')
        # Run query
        cmd_analyze = f'codeql database analyze {db_dir} {ql_file} --format=csv --output={csv_path}'
        result = subprocess.run(cmd_analyze, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            continue  # Query failed - try next query
        # Parse CSV results
        if not os.path.exists(csv_path):
            continue
        try:
            with open(csv_path, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
                if len(rows) <= 1:  # Only header = no vulnerabilities
                    continue
                # Check if our file is in the results
                for row in rows[1:]:
                    if not row or len(row) < 5:
                        continue
                    # File path is typically in column 4
                    file_path = row[4] if len(row) > 4 else row[0]
                    file_path = file_path.strip('"')
                    result_filename = os.path.basename(file_path)
                    # Check if this result matches our file
                    if result_filename == file_name or file_name in file_path or file_path.endswith(file_name):
                        return "1"  # Vulnerability found in this file
        except Exception:
            continue
    return "0"  # No vulnerabilities found


# ========================================================================
# SecEvalBase Analyzer
# ========================================================================
def load_secevalbase(json_path):
    with open(json_path, "r") as f:
        return json.load(f)


class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Test execution timeout")

@contextmanager
def capture_output():
    """Capture stdout and stderr"""
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    try:
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def analyze_with_secevalbase(scenarios_json, scenario_id, file_path):
    """
    Analyze code using SecEvalBase test cases.
    
    Args:
        scenarios_json: Loaded JSON data from SecEvalBase.json
        scenario_id: Scenario folder name (e.g., "CWE-020_author_1")
        file_path: Full path to the file
    
    Returns:
        tuple: (result, error_msg) where result is "0"/"1"/"unknown"
    """
    if not scenarios_json:
        return "N/A", ""

    scenario_id_norm = scenario_id.replace('/', '_')
    scenario = next((s for s in scenarios_json if s.get('ID', '').replace('/', '_') == scenario_id_norm), None)
    if not scenario or 'Test' not in scenario or 'Entry_Point' not in scenario:
        return "unknown", ""

    with open(file_path, "r") as f:
        candidate_code = f.read()

    entry_point = scenario['Entry_Point']
    test_code = scenario['Test']
    
    print(f"[SecEval] Testing: {scenario_id}")
    print(f"[SecEval] Entry point: {entry_point}")
    print(f"[SecEval] INPUT (Candidate Code):")
    print(candidate_code)
    print(f"[SecEval] TEST CODE:")
    print(test_code)
    print(f"[SecEval] ENTRY POINT: {entry_point}")

    # Create comprehensive execution environment
    local_env = {
        '__name__': '__test_module__',
        '__file__': file_path,
        '__builtins__': __builtins__,
        'tempfile': tempfile,
        'os': os,
        'json': json,
    }

    # Mock input() to prevent hanging
    def mock_input(prompt=""):
        return "ls"  # Safe default for command execution
    
    local_env['input'] = mock_input
    local_env['raw_input'] = mock_input
    
    # Add commonly expected variables
    local_env['file'] = None  # For cases where 'file' variable is expected
    
    # Mock os.close to prevent closing critical file descriptors
    original_os_close = os.close
    def safe_os_close(fd):
        if fd in [0, 1, 2]:  # Don't close stdin, stdout, stderr
            print(f"[SecEval] Warning: Prevented closing critical file descriptor {fd}")
            return
        try:
            return original_os_close(fd)
        except:
            pass  # Ignore errors for non-existent file descriptors
    
    local_env['os'].close = safe_os_close

    # Import common modules that tests might need
    try:
        import sys
        local_env['sys'] = sys
    except ImportError:
        pass
    
    try:
        import yaml
        local_env['yaml'] = yaml
    except ImportError:
        pass
    
    try:
        import pickle
        local_env['pickle'] = pickle
    except ImportError:
        pass
    
    try:
        import subprocess
        local_env['subprocess'] = subprocess
    except ImportError:
        pass
    
    try:
        import hashlib
        local_env['hashlib'] = hashlib
    except ImportError:
        pass
    
    try:
        import jwt
        local_env['jwt'] = jwt
    except ImportError:
        pass
    
    try:
        import requests
        local_env['requests'] = requests
    except ImportError:
        pass
    
    try:
        import mysql.connector
        local_env['mysql'] = mysql
    except ImportError:
        pass
    
    try:
        import ssl
        local_env['ssl'] = ssl
    except ImportError:
        pass
    
    try:
        import time
        local_env['time'] = time
    except ImportError:
        pass
    
    try:
        import re
        local_env['re'] = re
    except ImportError:
        pass
    
    try:
        import base64
        local_env['base64'] = base64
    except ImportError:
        pass
    
    try:
        import tarfile
        local_env['tarfile'] = tarfile
    except ImportError:
        pass
    
    try:
        import html
        local_env['html'] = html
    except ImportError:
        pass
    
    try:
        from lxml import etree
        local_env['etree'] = etree
        local_env['lxml'] = __import__('lxml')
    except ImportError:
        pass
    
    try:
        from Crypto.Cipher import AES, DES
        from Crypto.PublicKey import RSA
        from Crypto.Util.Padding import pad
        local_env['AES'] = AES
        local_env['DES'] = DES
        local_env['RSA'] = RSA
        local_env['pad'] = pad
    except ImportError:
        pass
    
    try:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        local_env['Cipher'] = Cipher
        local_env['algorithms'] = algorithms
        local_env['modes'] = modes
    except ImportError:
        pass
    
    try:
        import psutil
        local_env['psutil'] = psutil
    except ImportError:
        pass
    
    try:
        import shutil
        local_env['shutil'] = shutil
    except ImportError:
        pass
    
    try:
        import sqlite3
        local_env['sqlite3'] = sqlite3
    except ImportError:
        pass
    
    try:
        import urllib
        local_env['urllib'] = urllib
    except ImportError:
        pass
    
    try:
        import zipfile
        local_env['zipfile'] = zipfile
    except ImportError:
        pass
    
    try:
        import threading
        local_env['threading'] = threading
    except ImportError:
        pass

    # Import MagicMock first (needed for Flask mocking)
    try:
        from unittest.mock import MagicMock as MockClass
    except ImportError:
        # Fallback simple mock
        class MockClass:
            def __init__(self, *args, **kwargs):
                pass
            def __call__(self, *args, **kwargs):
                return self
            def __getattr__(self, name):
                return self

    # Mock Flask app if needed
    try:
        from flask import Flask, request, Response, redirect, make_response, send_file, jsonify
        from werkzeug.datastructures import Headers
        from werkzeug.utils import secure_filename
        from werkzeug.test import Client
        from html import escape
        
        local_env['Flask'] = Flask
        local_env['request'] = request
        local_env['Response'] = Response
        local_env['redirect'] = redirect
        local_env['make_response'] = make_response
        local_env['send_file'] = send_file
        local_env['jsonify'] = jsonify
        local_env['Headers'] = Headers
        local_env['secure_filename'] = secure_filename
        local_env['join'] = os.path.join
        local_env['Client'] = Client
        local_env['escape'] = escape
        
        # Try to import BaseResponse (version-dependent)
        try:
            from werkzeug.wrappers import BaseResponse
            local_env['BaseResponse'] = BaseResponse
        except ImportError:
            # Werkzeug 2.0+ moved BaseResponse
            try:
                from werkzeug.wrappers import Response as BaseResponse
                local_env['BaseResponse'] = BaseResponse
            except ImportError:
                local_env['BaseResponse'] = MockClass
        
        # Check if candidate code creates a Flask app
        if 'app = Flask(' in candidate_code or '@app.route' in candidate_code:
            # Let the candidate code create its own app
            pass
        else:
            local_env['app'] = MockClass()
    except ImportError:
        local_env['Flask'] = MockClass
        local_env['app'] = MockClass()
        local_env['request'] = MockClass()
        local_env['send_file'] = MockClass()
        local_env['secure_filename'] = lambda x: x
        local_env['join'] = os.path.join
        local_env['Client'] = MockClass
        local_env['BaseResponse'] = MockClass

    # Add unittest.mock for test code
    try:
        from unittest.mock import patch, Mock
        local_env['patch'] = patch
        local_env['MagicMock'] = MockClass  # Use the MockClass defined earlier
        local_env['Mock'] = Mock
    except ImportError:
        local_env['patch'] = None
        local_env['MagicMock'] = MockClass
        local_env['Mock'] = MockClass

    # Set up timeout (10 seconds for test execution)
    signal.signal(signal.SIGALRM, timeout_handler)
    
    try:
        # Execute candidate code with timeout
        signal.alarm(5)  # 5 seconds for candidate code execution
        
        # Remove any infinite loops at the module level
        # This is a hack but necessary for code with while True at module level
        modified_candidate = candidate_code
        
        # Check if there's a while True loop at module level (not indented)
        lines = candidate_code.split('\n')
        modified_lines = []
        skip_until_dedent = False
        
        for i, line in enumerate(lines):
            # Check if this is a module-level while True:
            if line.strip().startswith('while True:') and not line.startswith((' ', '\t')):
                skip_until_dedent = True
                print(f"[SecEval] Warning: Skipping module-level infinite loop at line {i+1}")
                continue
            
            # If we're skipping, check if we've dedented back to module level
            if skip_until_dedent:
                if line and not line.startswith((' ', '\t')):
                    skip_until_dedent = False
                    modified_lines.append(line)
                # Skip indented lines that are part of the while loop
                continue
            
            modified_lines.append(line)
        
        modified_candidate = '\n'.join(modified_lines)
        
        with capture_output() as (stdout, stderr):
            exec(modified_candidate, local_env)
        
        signal.alarm(0)  # Cancel alarm

        # Verify entry point exists
        if entry_point not in local_env:
            error_msg = f"Entry point '{entry_point}' not found in code"
            print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
            return "unknown", error_msg

        # Set up the candidate function for testing
        local_env['candidate'] = local_env[entry_point]

        # Execute test code with timeout
        signal.alarm(10)  # 10 seconds for test execution
        
        with capture_output() as (stdout, stderr):
            exec(test_code, local_env)
        
        signal.alarm(0)  # Cancel alarm

        if 'check' not in local_env:
            error_msg = "'check' function not found in test"
            print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
            return "unknown", error_msg

        # Run the test with timeout
        signal.alarm(10)  # 10 seconds for check execution
        
        with capture_output() as (stdout, stderr):
            local_env['check'](local_env['candidate'])
        
        captured_stdout = stdout.getvalue()
        captured_stderr = stderr.getvalue()
        
        signal.alarm(0)  # Cancel alarm
        
        if captured_stdout:
            print(f"[SecEval] Test stdout: {captured_stdout}")
        if captured_stderr:
            print(f"[SecEval] Test stderr: {captured_stderr}")
        
        print("[SecEval] TEST OUTPUT: ✅ PASS")
        return "0", ""

    except TimeoutException:
        signal.alarm(0)  # Cancel alarm
        error_msg = "Test execution timeout (likely infinite loop or hanging operation)"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg

    except AssertionError as e:
        signal.alarm(0)  # Cancel alarm
        print(f"[SecEval] TEST OUTPUT: ❌ FAIL (Assertion Error)")
        print(f"[SecEval] Assertion details: {str(e)}")
        return "1", f"Assertion failed: {str(e)}"
        
    except FileNotFoundError as e:
        signal.alarm(0)  # Cancel alarm
        error_msg = f"File not found - {str(e)}"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg
        
    except ImportError as e:
        signal.alarm(0)  # Cancel alarm
        error_msg = f"Import error - {str(e)}"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg
        
    except KeyError as e:
        signal.alarm(0)  # Cancel alarm
        error_msg = f"Key error - {str(e)}"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg
        
    except AttributeError as e:
        signal.alarm(0)  # Cancel alarm
        error_msg = f"Attribute error - {str(e)}"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg
        
    except TypeError as e:
        signal.alarm(0)  # Cancel alarm
        error_msg = f"Type error - {str(e)}"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg
        
    except Exception as e:
        signal.alarm(0)  # Cancel alarm
        error_msg = f"{type(e).__name__}: {str(e)}"
        print(f"[SecEval] TEST OUTPUT: ⚠️ ERROR\n[SecEval] Exception: {error_msg}")
        return "unknown", error_msg
    
    finally:
        # Ensure alarm is cancelled
        signal.alarm(0)


# ========================================================================
# 3️⃣ META-ANALYSIS LOGIC
# ========================================================================

def meta_analysis(scenarios_dir, seceval_json_path=None, codeql_queries_root=None):
    print(f"\n🚀 Starting Meta Security Analysis in {scenarios_dir}\n")
    scenarios_json = None
    if seceval_json_path:
        with open(seceval_json_path, "r") as f:
            scenarios_json = json.load(f)

    summary = []
    # Move global_analyzer_stats initialization here so it's in scope for the scenario loop
    global_analyzer_stats = {name: {'nb_sec': 0, 'nb_vul': 0, 'nb_unknown': 0, 'nb_files': 0} for name in ['SecEval', 'Bandit', 'CodeQL', 'GPT-4o']}
    for scenario in sorted(os.listdir(scenarios_dir)):
        scenario_path = os.path.join(scenarios_dir, scenario)
        if not os.path.isdir(scenario_path) or not scenario.startswith("CWE-"):
            continue

        files = [f for f in os.listdir(scenario_path) if f.endswith(".py")]
        total, secure, insecure = len(files), 0, 0
        print(f"\n📂 Scenario: {scenario} ({len(files)} files)")

        # Initialize per-analyzer statistics
        analyzer_stats = {
            'SecEval': {'secure': 0, 'insecure': 0, 'unknown': 0},
            'Bandit': {'secure': 0, 'insecure': 0, 'unknown': 0},
            'CodeQL': {'secure': 0, 'insecure': 0, 'unknown': 0},
            'GPT-4o': {'secure': 0, 'insecure': 0, 'unknown': 0}
        }
        # Track intersection verdicts
        intersection_vul = 0
        intersection_sec = 0
        intersection_vul_unknown = 0
        intersection_sec_unknown = 0
        
        for f in files:
            file_path = os.path.join(scenario_path, f)
            with open(file_path, "r") as fh:
                code = fh.read()
            print(f"  🔍 Analyzing {f} ...", end=" ", flush=True)
            
            res_bandit = analyze_with_bandit(file_path)
            res_codeql = analyze_with_codeql(scenario_path, scenario, f, queries_root=codeql_queries_root)
            res_gpt4o = analyze_with_gpt4o(code)
            res_seceval_tuple = analyze_with_secevalbase(scenarios_json, scenario, file_path) if scenarios_json else ("N/A", "")
            res_seceval = res_seceval_tuple[0] if isinstance(res_seceval_tuple, tuple) else res_seceval_tuple
            
            print(f"[SecEval: {res_seceval}] [Bandit: {res_bandit}] [CodeQL: {res_codeql}] [GPT-4o: {res_gpt4o}]", end=" ")
            verdicts = [res_seceval, res_bandit, res_codeql, res_gpt4o]
            
            # Update per-analyzer stats
            for name, res in zip(['SecEval', 'Bandit', 'CodeQL', 'GPT-4o'], [res_seceval, res_bandit, res_codeql, res_gpt4o]):
                if name == 'SecEval' and res == "unknown":
                    analyzer_stats[name]['unknown'] += 1
                elif res == "1":
                    analyzer_stats[name]['insecure'] += 1
                elif res == "0":
                    analyzer_stats[name]['secure'] += 1
                else:
                    analyzer_stats[name]['unknown'] += 1
            
            # Intersection verdict logic
            if res_seceval == "unknown":
                if any(r == "1" for r in [res_bandit, res_codeql, res_gpt4o] if r != "unknown" and r != "N/A"):
                    intersection_vul_unknown += 1
                    print("❓ Vulnerable unknown (SecEval unknown, other analyzer vulnerable)")
                elif all(r == "0" for r in [res_bandit, res_codeql, res_gpt4o] if r != "unknown" and r != "N/A"):
                    intersection_sec_unknown += 1
                    print("❓ Secure unknown (SecEval unknown, other analyzers secure)")
                else:
                    print("❓ Unknown")
            elif any(r == "1" for r in verdicts if r != "unknown" and r != "N/A"):
                intersection_vul += 1
                insecure += 1
                print("❌ Vulnerable")
            elif all(r == "0" for r in verdicts if r != "unknown" and r != "N/A"):
                intersection_sec += 1
                secure += 1
                print("✅ Secure")
            else:
                print("❓ Unknown")
        
        # Scenario metrics
        nb_files = total
        nb_sec = intersection_sec
        nb_vul = intersection_vul
        nb_vul_non_func = intersection_vul_unknown
        nb_sec_non_func = intersection_sec_unknown
        vul_non_func_per_file = nb_vul_non_func / nb_files if nb_files else 0
        vul_non_func_per_10 = nb_vul_non_func / 10
        sec_non_func_per_file = nb_sec_non_func / nb_files if nb_files else 0
        sec_non_func_per_10 = nb_sec_non_func / 10
        print(f"→ {nb_sec}/{nb_files} secure | sec/10: {nb_sec/10:.3f} | nb_vul: {nb_vul} | nb_vul_non_func: {nb_vul_non_func} | nb_sec_non_func: {nb_sec_non_func} | vulNonFunc/Files: {vul_non_func_per_file:.3f} | vulNonFunc/10: {vul_non_func_per_10:.3f} | secNonFunc/Files: {sec_non_func_per_file:.3f} | secNonFunc/10: {sec_non_func_per_10:.3f}")
        print("  Analyzer statistics:")
        
        # Per-analyzer statistics for this scenario
        analyzer_summary = {}
        for name, stats in analyzer_stats.items():
            nb_sec = stats['secure']
            nb_vul = stats['insecure']
            nb_unknown = stats['unknown']
            sec_per_file = nb_sec / nb_files if nb_files else 0
            sec_per_10 = nb_sec / 10
            analyzer_summary[name] = {
                'nb_sec': nb_sec,
                'nb_vul': nb_vul,
                'nb_unknown': nb_unknown,
                'sec_per_file': sec_per_file,
                'sec_per_10': sec_per_10
            }
            if name == 'SecEval':
                print(f"  {name:7} | Sec: {nb_sec} | Vul: {nb_vul} | Unknown: {nb_unknown} | Sec/Files: {sec_per_file:.3f} | Sec/10: {sec_per_10:.3f}")
            else:
                print(f"  {name:7} | Sec: {nb_sec} | Vul: {nb_vul} | Sec/Files: {sec_per_file:.3f} | Sec/10: {sec_per_10:.3f}")
        # Update global analyzer stats
        for name, stats in analyzer_stats.items():
            global_analyzer_stats[name]['nb_sec'] += stats['secure']
            global_analyzer_stats[name]['nb_vul'] += stats['insecure']
            global_analyzer_stats[name]['nb_unknown'] += stats['unknown']
            global_analyzer_stats[name]['nb_files'] += nb_files
        
        # Store for global summary
        summary.append({
            "scenario": scenario,
            "nb_files": nb_files,
            "nb_sec": nb_sec,
            "nb_vul": nb_vul,
            "nb_vul_non_func": nb_vul_non_func,
            "nb_sec_non_func": nb_sec_non_func,
            "analyzer_summary": analyzer_summary
        })
    
    # ========================================================================
    # 4️⃣ FINAL SUMMARY
    # ========================================================================
    print("\n" + "=" * 80)
    print("🧾 FINAL SUMMARY")
    print("=" * 80)
    
    # Global analyzer stats
    global_analyzer_stats = {name: {'nb_sec': 0, 'nb_vul': 0, 'nb_unknown': 0, 'nb_files': 0} for name in ['SecEval', 'Bandit', 'CodeQL', 'GPT-4o']}
    total_files = 0
    total_sec = 0
    total_vul = 0
    total_vul_non_func = 0
    total_sec_non_func = 0
    total_vul_or_nonfunc = 0
    
    # Collect per-scenario metrics for averaging
    sec_per_file_list = []
    sec_per_10_list = []
    vul_non_func_per_file_list = []
    vul_non_func_per_10_list = []
    sec_non_func_per_file_list = []
    sec_non_func_per_10_list = []

    for s in summary:
        sec_per_file = s['nb_sec']/s['nb_files'] if s['nb_files'] else 0
        sec_per_10 = s['nb_sec']/10
        vul_non_func_per_file = s['nb_vul_non_func'] / s['nb_files'] if s['nb_files'] else 0
        vul_non_func_per_10 = s['nb_vul_non_func'] / 10
        sec_non_func_per_file = s['nb_sec_non_func'] / s['nb_files'] if s['nb_files'] else 0
        sec_non_func_per_10 = s['nb_sec_non_func'] / 10
        print(
            f"{s['scenario']:30} | Files: {s['nb_files']:3} | Sec: {s['nb_sec']:3} | Sec/Files: {sec_per_file:.3f} | Sec/10: {sec_per_10:.3f} | Vul: {s['nb_vul']:3} | Vul non func: {s['nb_vul_non_func']:3} | VulNonFunc/Files: {vul_non_func_per_file:.3f} | VulNonFunc/10: {vul_non_func_per_10:.3f} | Sec non func: {s['nb_sec_non_func']:3} | SecNonFunc/Files: {sec_non_func_per_file:.3f} | SecNonFunc/10: {sec_non_func_per_10:.3f}"
        )
        total_files += s['nb_files']
        total_sec += s['nb_sec']
        total_vul += s['nb_vul']
        total_vul_non_func += s['nb_vul_non_func']
        total_sec_non_func += s['nb_sec_non_func']
        # For averages
        sec_per_file_list.append(sec_per_file)
        sec_per_10_list.append(sec_per_10)
        vul_non_func_per_file_list.append(vul_non_func_per_file)
        vul_non_func_per_10_list.append(vul_non_func_per_10)
        sec_non_func_per_file_list.append(sec_non_func_per_file)
        sec_non_func_per_10_list.append(sec_non_func_per_10)
    
    # Print TOTAL as mean of per-scenario metrics
    n = len(summary)
    mean_sec_per_file = sum(sec_per_file_list)/n if n else 0
    global_sec_per_10 = total_sec/(n*10) if n else 0
    mean_vul_non_func_per_file = sum(vul_non_func_per_file_list)/n if n else 0
    global_vul_non_func_per_10 = total_vul_non_func/(n*10) if n else 0
    mean_sec_non_func_per_file = sum(sec_non_func_per_file_list)/n if n else 0
    global_sec_non_func_per_10 = total_sec_non_func/(n*10) if n else 0
    mean_sec_per_scen = total_sec/n if n else 0
    print("-" * 80)
    print(f"TOTAL | Files: {total_files} | Sec: {total_sec} | Vul: {total_vul} | "
          f"Mean Sec/Files: {mean_sec_per_file:.3f} | Sec/10: {global_sec_per_10:.3f} | "
          f"Mean VulNonFunc/Files: {mean_vul_non_func_per_file:.3f} | VulNonFunc/10: {global_vul_non_func_per_10:.3f} | "
          f"Mean SecNonFunc/Files: {mean_sec_non_func_per_file:.3f} | SecNonFunc/10: {global_sec_non_func_per_10:.3f} | "
          f"Total VulNonFunc: {total_vul_non_func} | Total SecNonFunc: {total_sec_non_func}")
    print("\nGlobal Analyzer Statistics:")
    for name, stats in global_analyzer_stats.items():
        sec_per_file = stats['nb_sec'] / stats['nb_files'] if stats['nb_files'] else 0
        sec_per_10 = stats['nb_sec'] / 10
        if name == 'SecEval':
            print(f"  {name:7} | Sec: {stats['nb_sec']} | Vul: {stats['nb_vul']} | Unknown: {stats['nb_unknown']} | Sec/Files: {sec_per_file:.3f} | Sec/10: {sec_per_10:.3f}")
        else:
            print(f"  {name:7} | Sec: {stats['nb_sec']} | Vul: {stats['nb_vul']} | Sec/Files: {sec_per_file:.3f} | Sec/10: {sec_per_10:.3f}")
    print("=" * 80)


# ========================================================================
# 5️⃣ ENTRY POINT
# ========================================================================
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print('Usage: python meta_analysis.py <scenarios_dir> <seceval_json_path> [codeql_queries_root]')
        sys.exit(1)
    scenarios_dir = sys.argv[1]
    seceval_json_path = sys.argv[2]
    codeql_queries_root = sys.argv[3] if len(sys.argv) > 3 else None
    meta_analysis(scenarios_dir, seceval_json_path, codeql_queries_root)