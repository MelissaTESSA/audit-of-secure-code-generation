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
