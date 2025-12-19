# Adversarial Audit of Secure Code Generation

> **⚠️ This is the anonymised artifact repo for the AsiaCCS’26 paper.**  
> **Permanent link:** [https://anonymous.4open.science/r/audit-of-secure-code-generation-53E6/](https://anonymous.4open.science/r/audit-of-secure-code-generation-53E6/)

This repository contains **code, data, and scripts** required to reproduce the three-phase adversarial robustness evaluation of three state-of-the-art secure code generation methods:

- **Sven** – prefix-tuning (white-box)  
- **SafeCoder** – LoRA instruction tuning (white-box)  
- **PromSec** – black-box prompt optimization  

The audit shows that **security guarantees collapse to 3–17%** under realistic prompt perturbations once *both* security and functionality are enforced.

---

## ▶️ Running Experiments

### Phase 1 – Robustness Under Adversarial Conditions

Phase 1  reproduces the original evaluation protocols and metrics reported by each method, using the authors’ official released artifacts. No unified benchmark or additional checks are applied at this stage.

The goal is to verify whether the claimed security guarantees hold under adversarial prompt perturbations, without changing the original evaluation setup.

Summary of steps for each method:

```bash
git clone https://anonymous.4open.science/r/audit-of-secure-code-generation-53E6/
cd audit-of-secure-code-generation-53E6
```
### 1️⃣ PromSec (Black-box Prompt Optimization)

- **Repository:** https://github.com/mahmoudkanazzal/PromSec

**What we reproduce:**
- Original PromSec repair loop
- Security evaluation using Bandit (Python) and SpotBugs (Java)
- Functional preservation via graph similarity and fuzzing, as in the paper

**Setup:**
```bash
cd PromSec
```
Set up Python dependencies (a virtual environment is recommended)
```bash
conda create -n promsec_env python=3.10 -y
conda activate promsec_env
```
Install required packages: (Python 3.x, PyTorch, PyTorch Geometric, NetworkX, Matplotlib, OpenAI API, Bandit)

Set your OPENAI_API_KEY

Execute the cells of Demo_PromSec_PoC_Oct_2024_public.ipynb on the original Testing_DS from the PromSec paper
**🧩 Reproducing Results Under Prompt Perturbation**


To reproduce the results under prompt perturbation, you should use the perturbed datasets provided in this repository under PromSec directory. In the notebook `Demo_PromSec_PoC_Oct_2024_public.ipynb`, search for all occurrences of `Testing_DS` (using Ctrl+F or your editor’s search function) and replace them with the desired perturbed dataset name, for example:

- `Testing_DS_VulComments` – for samples with vulnerable comments
- `Testing_DS_DeadCode` – for samples with dead code
- (Other `Testing_DS_x` variants as provided)

These datasets contain the perturbed samples derived from the original `Testing_DS`. This allows you to evaluate the robustness of the methods under different types of prompt perturbations, following the same evaluation protocol as for the original dataset.

### 2️⃣ SVEN (Prefix-Tuning for Secure Code Generation)

- **Repository:** [https://github.com/eth-sri/sven](https://github.com/eth-sri/sven)

**What we reproduce:**

- Official SVEN secure / vulnerable prefixes  
- Prefix-controlled code generation  
- Security evaluation using **CodeQL**  
- Functionality evaluation using **HumanEval (Pass@k)**  

**Setup:**

```bash
cd sven
```
Create virtual environment
```bash
conda create -n sven_env python=3.10 -y
conda activate sven_env
```
 Set up Python dependencies and CodeQL
```bash
pip install -r requirements.txt
pip install -e .
./setup_codeql.sh
```

To evaluate the security of the original LLM, run the command below. The model 350m can be replaced by {2b, 6b}
```bash
cd scripts
python sec_eval.py --model_type prefix \
                   --model_dir ../trained/350m-prefix/checkpoint-last \
                   --output_name sec-eval-350m-prefix

python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-350m-lm
```
We use the HumanEval benchmark from the MultiPL-E framework to evaluate functional correctness. For SVEN, we need to run the two branches sec and vul separately via the --control argument. The command below is for the sec branch:

```bash
python human_eval_gen.py --model_type prefix \
                         --model_dir ../trained/350m-prefix/checkpoint-last \
                         --control sec \
                         --output_name human-eval-350m-prefix-sec

python human_eval_exec.py --output_name human-eval-350m-prefix-sec
```
To view the results, run:
```bash
python print_results.py --eval_type human_eval \
                        --eval_dir ../experiments/human_eval/human-eval-350m-prefix-sec
```
**🧩 Reproducing Results Under Prompt Perturbation**


To reproduce results under prompt perturbation for SVEN, use the perturbed datasets provided in the `sven/data_eval` directory (e.g., `train_CommentToQuestion`, `train_OneComment`, `trained_append_10lines`, etc.).

**How to use a perturbed dataset:**

In your evaluation command, change the `--data_dir` argument to point to the desired perturbed dataset.  
For example, to evaluate on `trained_append_10lines`:

```bash
# 350m-prefix on trained_append_10lines
python sec_eval.py --model_type prefix --model_dir ../trained/350m-prefix/checkpoint-last --output_name sec-eval-350m-prefix --data_dir ../data_eval/trained_append_10lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-350m-prefix
```

### 3️⃣ SafeCoder (Instruction-Tuned Secure Generation)

- **Repository:** [https://github.com/eth-sri/SafeCoder](https://github.com/eth-sri/SafeCoder)

**What we reproduce:**

- Released LoRA-finetuned checkpoints  
- Instruction-following secure code generation  
- Security evaluation using **CodeQL**  
- Functionality evaluation on **HumanEval**, **MBPP**, **MMLU**, and **TruthfulQA**  

**Setup:**

```bash
cd SafeCoder

# Install Python dependencies (virtual environment recommended)
pip install -r requirements.txt
pip install -e .

# Install GitHub CodeQL
./setup_codeql.sh
Cd scripts
```
To evaluate the security of generated code, run the following commands:
```bash
python sec_eval.py \
  --output_name codellama-7b-safecoder \
  --model_name codellama-7b-lora-safecoder \
  --eval_type trained \
  --num_samples 100 \
  --num_samples_per_gen 20 \
  --temp 0.4 \
  --max_gen_len 256 \
  --top_p 0.95 \
  --vul_type "" \
  --experiments_dir /home/melissa/SafeCoder/experiments \
  --data_dir /home/melissa/SafeCoder/data_eval/sec_eval \
  --model_dir /home/melissa/SafeCoder

python print_results.py \
  --eval_name codellama-7b-safecoder \
  --eval_type trained \
  --detail
```

For utility, we consider the following benchmarks:
```bash
# HumanEval
./func_eval.sh human_eval codellama-7b-safecoder-0.4 codellama-7b-lora-safecoder 0.4
python print_results.py --eval_name codellama-7b-safecoder-0.4 --eval_type human_eval

# MBPP
./func_eval.sh mbpp codellama-7b-safecoder-0.4 codellama-7b-lora-safecoder 0.4
python print_results.py --eval_name codellama-7b-safecoder-0.4 --eval_type mbpp

# MMLU
python mmlu_eval.py --output_name codellama-7b-safecoder --model_name codellama-7b-lora-safecoder
python print_results.py --eval_name codellama-7b-safecoder --eval_type mmlu

# TruthfulQA
python truthfulqa_eval.py --output_name codellama-7b-safecoder --model_name codellama-7b-lora-safecoder
python print_results.py --eval_name codellama-7b-safecoder --eval_type tqa
```
**🧩 Reproducing Results Under Prompt Perturbation**


To reproduce results under prompt perturbation for SafeCoder, use the perturbed datasets provided in the `sven/data_eval/sec_eval` directory (e.g., `train_CommentToQuestion`, `train_OneComment`, `trained_append_10lines`, etc.).

**How to use a perturbed dataset:**

In your evaluation command, change the `--data_dir` argument to point to the desired perturbed dataset.  
For example, to evaluate on `trained_append_10lines`:

```bash
# Go to the scripts directory if not already there
cd scripts

# Activate your environment (if not already active)
source ../safecoder_env/bin/activate

# Set the PYTHONPATH
export PYTHONPATH=..

# Prepare the temporary data directory and symlink for the perturbed dataset
mkdir -p ../data_eval/temp_trained_append_10lines
rm -f ../data_eval/temp_trained_append_10lines/trained
ln -s ../data_eval/sec_eval/trained_append_10lines ../data_eval/temp_trained_append_10lines/trained

# Run the evaluation
python sec_eval.py \
  --output_name codellama-7b-safecoder_trained_append_10lines \
  --model_name codellama-7b-lora-safecoder \
  --eval_type trained \
  --num_samples 100 \
  --num_samples_per_gen 20 \
  --experiments_dir ../experiments \
  --data_dir ../data_eval/temp_trained_append_10lines \
  --model_dir ..

# To use another perturbation, replace 'trained_append_10lines' everywhere above with your dataset name (e.g., train_CommentToQuestion)
```
### Phase 2 – Unified Benchmarking Analysis
In Phase 2, we run all three models on the same CodeSecEval benchmark and keep only snippets that pass every static analyser (CodeQL, Bandit, GPT-4o) and the unit tests—no partial credit. This gives the first apples-to-apples baseline of true secure-and-functional code before any adversarial twist.
### 1️⃣ PromSec
Open and run every cell of **Demo_PromSec_PoC_Oct_2024_public_1.ipynb** in the PromSec folder; the notebook feeds the unified CodeSecEval tasks through the original repair loop and records the consensus secure-and-functional rate.
### 2️⃣ SVEN
Run the unified evaluation on CodeSecEval benchmark and collect consensus scores:

```bash
cd sven/scripts
python sec_eval_unified.py \
  --output_name SecEval_Analysis \
  --new_dataset_json ../../CodeSecEval/SecEvalBase/SecEvalBase.json \
  --model_type prefix \
  --model_dir ../trained/2b-prefix/checkpoint-last \
  --temp 0.4 \
  --num_gen 10

python all_analyzers.py \
  ../experiments/sec_eval/SecEval_Student_Analysis/trained/new_dataset \
  ../../CodeSecEval/SecEvalBase/SecEvalBase.json \
  | tee codeseceval.txt
```
### 3️⃣ SafeCoder
Run the unified evaluation on CodeSecEval benchmark and collect consensus scores:
```bash
python sec_eval_unified.py \
  --output_name my_eval_run_secevalbase \
  --eval_type trained \
  --model_name codellama-7b-lora-safecoder \
  --model_dir .. \
  --codesec_json ../CodeSecEval/SecEvalBase/SecEvalBase.json

cd ../CodeSecEval/SecEvalBase && \
python ../../scripts/all_analyzers.py \
  ../../experiments/sec_eval/my_eval_run_secevalbase/trained \
  SecEvalBase.json | tee ../../scripts/codeseceval.txt

### Phase 3 – Robustness Under Adversarial Conditions in Unified Setting
### 1️⃣ PromSec
Continue with the two attack notebooks:

  **-Demo_PromSec_PoC_Oct_2024_public_Student.py** (natural student-style reframing)
  **-Demo_PromSec_PoC_Oct_2024_public_Inverse.ipynb** (cue-inversion that flips security guidance)
Running both repeats the unified evaluation while injecting the adversarial prompts, letting you measure how much the already-low baseline drops when the prompt is gently twisted.
### 2️⃣ SVEN
Run the unified evaluation on the **Student-rephrased** prompts from CodeSecEval and collect consensus scores:

```bash
cd sven/scripts
python sec_eval_unified.py \
  --output_name SecEval_Student_Analysis \
  --new_dataset_json ../../CodeSecEval-Student/SecEvalBase/SecEvalBase.json \
  --model_type prefix \
  --model_dir ../trained/2b-prefix/checkpoint-last \
  --temp 0.4 \
  --num_gen 10

python all_analyzers.py \
  ../experiments/sec_eval/SecEval_Student_Analysis/trained/new_dataset \
  ../../CodeSecEval-Student/SecEvalBase/SecEvalBase.json \
  | tee codeseceval_student.txt
```
For Inverse (cue-flip), replace every CodeSecEval-Student path with CodeSecEval-Inverse and change the output names accordingly.
### 3️⃣ SafeCoder

```bash
python sec_eval_unified.py \
  --output_name my_eval_run_secevalbase_student \
  --eval_type trained \
  --model_name codellama-7b-lora-safecoder \
  --model_dir .. \
  --codesec_json ../CodeSecEval-Student/SecEvalBase/SecEvalBase.json

cd ../CodeSecEval-Student/SecEvalBase && \
python ../../scripts/all_analyzers.py \
  ../../experiments/sec_eval/my_eval_run_secevalbase_student/trained \
  SecEvalBase.json | tee ../../scripts/codeseceval_student.txt
```

Replace every CodeSecEval-Student path with CodeSecEval-Inverse (and choose a fresh output name such as my_eval_run_secevalbase_inverse)
