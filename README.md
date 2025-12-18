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

### Phase 1 – Reproducing Original Evaluations (Quick Start)

Phase 1 strictly reproduces the original evaluation protocols and metrics reported by each method, using the authors’ official Quick Start instructions and released artifacts. No unified benchmark or additional checks are applied at this stage.

The goal is to verify whether the claimed security guarantees hold under adversarial prompt perturbations, without changing the original evaluation setup.

Summary of steps for each method:

```bash
git clone https://anonymous.4open.science/r/audit-of-secure-code-generation-53E6/
cd audit-of-secure-code-generation-53E6
```` ``` ````
### 1️⃣ PromSec (Black-box Prompt Optimization)

- **Repository:** https://github.com/mahmoudkanazzal/PromSec

**What we reproduce:**
- Original PromSec repair loop
- Security evaluation using Bandit (Python) and SpotBugs (Java)
- Functional preservation via graph similarity and fuzzing, as in the paper

**Setup:**
cd PromSec
# Set up Python dependencies (a virtual environment is recommended)
conda create -n promsec_env python=3.10 -y
conda activate promsec_env
# Install required packages: (Python 3.x, PyTorch, PyTorch Geometric, NetworkX, Matplotlib, OpenAI API, Bandit)
Set your OPENAI_API_KEY
Execute the cells of Demo_PromSec_PoC_Oct_2024_public.ipynb on the original Testing_DS from the PromSec paper
