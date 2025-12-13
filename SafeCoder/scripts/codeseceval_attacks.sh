#!/bin/bash

# SafeCoder Evaluation Script - Inverse and Student Datasets
# Runs codellama-7b-lora-safecoder on both inverse and student datasets with negative security comments

# Note: Not using set -e to allow script to continue even if some commands fail

echo "=== SAFECODER EVALUATION: INVERSE AND STUDENT DATASETS ==="
echo "Generated on: $(date)"
echo "Model: codellama-7b-lora-safecoder"
echo ""

# Ensure we're in the correct directory
cd ~/SafeCoder/scripts

# Activate virtual environment if not already active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating SafeCoder virtual environment..."
    cd ~/SafeCoder
    source safecoder_env/bin/activate
    cd scripts
fi

# Set environment variables
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# echo "🚀 Starting SafeCoder evaluation on Inverse dataset..."
# echo ""

# # Run evaluation on Inverse dataset
# PYTHONPATH=".:$PYTHONPATH" python sec_eval_unified.py \
#   --output_name my_eval_run_secevalbase_inverse \
#   --eval_type trained \
#   --model_name codellama-7b-lora-safecoder \
#   --model_dir /home/melissa/SafeCoder \
#   --codesec_json /home/melissa/CodeSecEval-Inverse/SecEvalBase/SecEvalBase.json || true

# echo ""
# echo "✅ Inverse dataset evaluation completed (or failed - continuing anyway)!"
# echo ""
# echo "========================================"
# echo ""

# echo "🚀 Starting SafeCoder evaluation on Student dataset..."
# echo ""

# # Run evaluation on Student dataset
# PYTHONPATH=".:$PYTHONPATH" python sec_eval_unified.py \
#   --output_name my_eval_run_secevalbase_student \
#   --eval_type trained \
#   --model_name codellama-7b-lora-safecoder \
#   --model_dir /home/melissa/SafeCoder \
#   --codesec_json /home/melissa/CodeSecEval-Student/SecEvalBase/SecEvalBase.json || true

# echo ""
# echo "✅ Student dataset evaluation completed (or failed - continuing anyway)!"
# echo ""
# echo "========================================"
# echo ""

# echo "🔍 Starting security analysis on Student dataset results..."
# echo ""

# # Run all_analyzers.py on Student dataset results
# cd /home/melissa/CodeSecEval-Student/SecEvalBase && python ~/SafeCoder/scripts/all_analyzers.py \
#   /home/melissa/SafeCoder/experiments/sec_eval/my_eval_run_secevalbase_student/trained \
#   /home/melissa/CodeSecEval-Student/SecEvalBase/SecEvalBase.json | tee /home/melissa/SafeCoder/scripts/codeseceval_attacks_student.txt || true
# cd ~/SafeCoder/scripts

# echo ""
# echo "✅ Student dataset security analysis completed (or failed - continuing anyway)!"
# echo ""
# echo "========================================"
# echo ""

# echo "🔍 Starting security analysis on Inverse dataset results..."
# echo ""

# # Run all_analyzers.py on Inverse dataset results
# cd /home/melissa/CodeSecEval-Inverse/SecEvalBase && python ~/SafeCoder/scripts/all_analyzers.py \
#   /home/melissa/SafeCoder/experiments/sec_eval/my_eval_run_secevalbase_inverse/trained \
#   /home/melissa/CodeSecEval-Inverse/SecEvalBase/SecEvalBase.json | tee /home/melissa/SafeCoder/scripts/codeseceval_attacks_inverse.txt || true
# cd ~/SafeCoder/scripts

# echo ""
# echo "✅ Inverse dataset security analysis completed (or failed - continuing anyway)!"
# echo ""
# echo "========================================"
# echo "🎉 All evaluations and security analysis completed successfully!"
# echo "📁 Results saved in experiments directory"
# echo "========================================"

echo "🚀 Starting SafeCoder evaluation on Base dataset..."
echo ""

# Run evaluation on Base dataset
PYTHONPATH=".:$PYTHONPATH" python sec_eval_unified.py \
  --output_name my_eval_run_secevalbase \
  --eval_type trained \
  --model_name codellama-7b-lora-safecoder \
  --model_dir /home/melissa/SafeCoder \
  --codesec_json /home/melissa/CodeSecEval/SecEvalBase/SecEvalBase.json || true

echo ""
echo "✅ Base dataset evaluation completed (or failed - continuing anyway)!"
echo ""
echo "========================================"
echo ""

echo "🔍 Starting security analysis on Base dataset results..."
echo ""

# Run all_analyzers.py on Base dataset results
cd /home/melissa/CodeSecEval/SecEvalBase && python ~/SafeCoder/scripts/all_analyzers.py \
  /home/melissa/SafeCoder/experiments/sec_eval/my_eval_run_secevalbase/trained \
  /home/melissa/CodeSecEval/SecEvalBase/SecEvalBase.json | tee /home/melissa/SafeCoder/scripts/codeseceval_attacks_base.txt || true
cd ~/SafeCoder/scripts

echo ""
echo "✅ Base dataset security analysis completed (or failed - continuing anyway)!"
echo ""
echo "========================================"
echo ""

echo "🚀 Starting SafeCoder evaluation on Plus dataset..."
echo ""

# Run evaluation on Plus dataset
PYTHONPATH=".:$PYTHONPATH" python sec_eval_unified.py \
  --output_name my_eval_run_secevalplus \
  --eval_type trained \
  --model_name codellama-7b-lora-safecoder \
  --model_dir /home/melissa/SafeCoder \
  --codesec_json /home/melissa/CodeSecEval/SecEvalPlus/SecEvalPlus.json || true

echo ""
echo "✅ Plus dataset evaluation completed (or failed - continuing anyway)!"
echo ""
echo "========================================"
echo ""

echo "🔍 Starting security analysis on Plus dataset results..."
echo ""

# Run all_analyzers.py on Plus dataset results
cd /home/melissa/CodeSecEval/SecEvalPlus && python ~/SafeCoder/scripts/all_analyzers.py \
  /home/melissa/SafeCoder/experiments/sec_eval/my_eval_run_secevalplus/trained \
  /home/melissa/CodeSecEval/SecEvalPlus/SecEvalPlus.json | tee /home/melissa/SafeCoder/scripts/codeseceval_attacks_plus.txt || true
cd ~/SafeCoder/scripts

echo ""
echo "✅ Plus dataset security analysis completed (or failed - continuing anyway)!"
echo ""
echo "========================================"
echo "🎉 All evaluations and security analysis completed successfully!"
echo "📁 Results saved in experiments directory"
echo "========================================"
