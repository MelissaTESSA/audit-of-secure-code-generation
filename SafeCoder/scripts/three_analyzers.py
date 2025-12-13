# meta_analysis.py
import os
import json
import subprocess
import tempfile
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from openai import OpenAI


# ========================================================================
# 1️⃣ SETUP MODELS & API
# ========================================================================

def load_qwen_model(model_name="Qwen/Qwen1.5-7B"):
    print(f"Loading Qwen model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)


def analyze_with_gpt4o(code):
    """Call GPT-4o via OpenAI API and return 1 if vulnerable else 0"""
    client = OpenAI()
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


def analyze_with_qwen(pipe, code):
    """Use local Qwen model to detect vulnerabilities"""
    prompt = (
        "You are a security expert. Analyze the following Python code for vulnerabilities. "
        "Respond ONLY with '1' if you find any vulnerability or potential vulnerability, "
        "or '0' if none. Put the digit on the first line, then a short explanation on the next line.\n\nCode:\n" + code
    )
    txt = pipe(prompt, max_new_tokens=128)[0]['generated_text']
    return "1" if "1" in txt.splitlines()[0].strip() else "0"


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


def analyze_with_codeql(file_path):
    """Analyze with CodeQL CLI"""
    try:
        tmp_db = tempfile.mkdtemp()
        subprocess.run(
            ["codeql", "database", "create", tmp_db, "--language=python", "--source-root", os.path.dirname(file_path)],
            check=True, capture_output=True
        )
        result = subprocess.run(
            ["codeql", "database", "analyze", tmp_db, "codeql/python-queries:Security", "--format=json"],
            capture_output=True, text=True
        )
        if "result" in result.stdout or "alert" in result.stdout:
            return "1"
    except Exception:
        pass
    return "0"


# ========================================================================
# 3️⃣ META-ANALYSIS LOGIC
# ========================================================================

def meta_analysis(scenarios_dir):
    print(f"\n🚀 Starting Meta Security Analysis in {scenarios_dir}\n")
    pipe = load_qwen_model("Qwen/Qwen1.5-7B")

    summary = []
    for scenario in sorted(os.listdir(scenarios_dir)):
        scenario_path = os.path.join(scenarios_dir, scenario)
        if not os.path.isdir(scenario_path) or not scenario.startswith("CWE-"):
            continue

        files = [f for f in os.listdir(scenario_path) if f.endswith(".py")]
        total, secure, insecure = len(files), 0, 0
        print(f"\n📂 Scenario: {scenario} ({len(files)} files)")

        for f in files:
            file_path = os.path.join(scenario_path, f)
            with open(file_path, "r") as fh:
                code = fh.read()

            print(f"  🔍 Analyzing {f} ...", end=" ", flush=True)

            res_bandit = analyze_with_bandit(file_path)
            res_codeql = analyze_with_codeql(file_path)
            res_gpt4o = analyze_with_gpt4o(code)
            # res_qwen = analyze_with_qwen(pipe, code)  # Qwen disabled

            print(f"[Bandit: {res_bandit}] [CodeQL: {res_codeql}] [GPT-4o: {res_gpt4o}]", end=" ")

            # Meta decision rule: vulnerable if any analyzer says 1
            verdict = "1" if any(r == "1" for r in [res_bandit, res_codeql, res_gpt4o]) else "0"
            if verdict == "1":
                insecure += 1
                print("❌ Vulnerable")
            else:
                secure += 1
                print("✅ Secure")

        # Scenario metrics
        pct = (secure / total * 100) if total else 0
        avg_ratio = secure / total if total else 0
        avg_ratio_10 = avg_ratio / 10

        summary.append({
            "scenario": scenario,
            "total_files": total,
            "secure": secure,
            "insecure": insecure,
            "pct_secure": pct,
            "avg_ratio": avg_ratio,
            "avg_ratio_10": avg_ratio_10
        })

        print(f"→ {secure}/{total} secure ({pct:.1f}%) | Avg: {avg_ratio:.3f} | Avg/10: {avg_ratio_10:.3f}")

    # ========================================================================
    # 4️⃣ FINAL SUMMARY
    # ========================================================================
    print("\n" + "=" * 80)
    print("🧾 FINAL SUMMARY")
    print("=" * 80)
    for s in summary:
        print(
            f"{s['scenario']:30} | Files: {s['total_files']:3} | "
            f"Secure: {s['secure']:3} | Insecure: {s['insecure']:3} | "
            f"{s['pct_secure']:5.1f}% | Avg: {s['avg_ratio']:.3f} | Avg/10: {s['avg_ratio_10']:.3f}"
        )

    all_secure = sum(s['secure'] for s in summary)
    all_total = sum(s['total_files'] for s in summary)
    global_avg = all_secure / all_total if all_total else 0
    global_avg_10 = global_avg / 10

    print("-" * 80)
    print(f"TOTAL | Secure: {all_secure} / {all_total} | Avg: {global_avg:.3f} | Avg/10: {global_avg_10:.3f}")
    print("=" * 80)


# ========================================================================
# 5️⃣ ENTRY POINT
# ========================================================================
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python meta_analysis.py <scenarios_dir>')
        sys.exit(1)
    scenarios_dir = sys.argv[1]
    meta_analysis(scenarios_dir)
