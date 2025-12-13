#!/bin/bash

# SafeCoder Evaluation Script - Inverse and Student Datasets
# Runs codellama-7b-lora-safecoder on both inverse and student datasets with negative security comments

set -e  # Exit on error

echo "=== SAFECODER EVALUATION: INVERSE AND STUDENT DATASETS ==="
echo "Generated on: $(date)"
echo "Model: codellama-7b-lora-safecoder"
echo ""

# Activate virtual environment if not already active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating SafeCoder virtual environment..."
    cd /home/melissa/SafeCoder
    source safecoder_env/bin/activate
    cd scripts
fi

# Set environment variables
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

echo "🚀 Starting SafeCoder evaluation on Inverse dataset..."
echo ""

# Run evaluation on Inverse dataset
PYTHONPATH=".:$PYTHONPATH" python sec_eval_unified.py \
  --output_name my_eval_run_secevalplus_inverse \
  --eval_type trained \
  --model_name codellama-7b-lora-safecoder \
  --model_dir /home/melissa/SafeCoder \
  --codesec_json /home/melissa/CodeSecEval-Inverse/SecEvalBase/SecEvalBase.json

echo ""
echo "✅ Inverse dataset evaluation completed!"
echo ""
echo "========================================"
echo ""

echo "🚀 Starting SafeCoder evaluation on Student dataset..."
echo ""

# Run evaluation on Student dataset
PYTHONPATH=".:$PYTHONPATH" python sec_eval_unified.py \
  --output_name my_eval_run_secevalplus_student \
  --eval_type trained \
  --model_name codellama-7b-lora-safecoder \
  --model_dir /home/melissa/SafeCoder \
  --codesec_json /home/melissa/CodeSecEval-Student/SecEvalBase/SecEvalBase.json

echo ""
echo "✅ Student dataset evaluation completed!"
echo ""
echo "========================================"
echo "🎉 All evaluations completed successfully!"
echo "📁 Results saved in experiments directory"
echo "========================================"
