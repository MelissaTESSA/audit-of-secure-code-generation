#!/bin/bash

# echo "Starting SecEval Analysis on Multiple Datasets..."

# # Navigate to scripts directory
# cd /home/melissa/sven/scripts

# # Run Student Dataset Analysis
# echo "=== Running SecEval Student Dataset Analysis ==="
# python sec_eval_unified.py \
#   --output_name SecEval_Student_Analysis \
#   --new_dataset_json /home/melissa/CodeSecEval-Student/SecEvalBase/SecEvalBase.json \
#   --model_type prefix \
#   --model_dir ../trained/2b-prefix/checkpoint-last \
#   --temp 0.4 \
#   --num_gen 10

# echo "Student analysis completed."

# # Run Inverse Dataset Analysis
# echo "=== Running SecEval Inverse Dataset Analysis ==="
# python sec_eval_unified.py \
#   --output_name SecEval_Inverse_Analysis \
#   --new_dataset_json /home/melissa/CodeSecEval-Inverse/SecEvalBase/SecEvalBase.json \
#   --model_type prefix \
#   --model_dir ../trained/2b-prefix/checkpoint-last \
#   --temp 0.4 \
#   --num_gen 10

# echo "Inverse analysis completed."

# # Run Base Dataset Analysis
# echo "=== Running SecEval Base Dataset Analysis ==="
# python sec_eval_unified.py \
#   --output_name SecEval_Base_Analysis \
#   --new_dataset_json /home/melissa/CodeSecEval/SecEvalBase/SecEvalBase.json \
#   --model_type prefix \
#   --model_dir ../trained/2b-prefix/checkpoint-last \
#   --temp 0.4 \
#   --num_gen 10

# echo "Base analysis completed."

# # Run SecEvalPlus Dataset Analysis
# echo "=== Running SecEvalPlus Dataset Analysis ==="
# python sec_eval_unified.py \
#   --output_name SecEval_Plus_Analysis \
#   --new_dataset_json /home/melissa/CodeSecEval/SecEvalPlus/SecEvalPlus.json \
#   --model_type prefix \
#   --model_dir ../trained/2b-prefix/checkpoint-last \
#   --temp 0.4 \
#   --num_gen 10 | tee sven_codeseceval.txt

# echo "SecEvalPlus analysis completed."

# echo "All SecEval analyses completed successfully!"
# echo "Results saved in: /home/melissa/sven/experiments/sec_eval/"

# ========================================================================
# ALL_ANALYZERS.PY COMMANDS - Meta Security Analysis
# ========================================================================

# Base dataset
#python /home/melissa/sven/scripts/all_analyzers.py /home/melissa/sven/experiments/sec_eval/SecEval_Base_Analysis/trained/new_dataset /home/melissa/CodeSecEval/SecEvalBase/SecEvalBase.json | tee /home/melissa/sven/scripts/codeseceval_base.txt

# Student dataset  
#python /home/melissa/sven/scripts/all_analyzers.py /home/melissa/sven/experiments/sec_eval/SecEval_Student_Analysis/trained/new_dataset /home/melissa/CodeSecEval-Student/SecEvalBase/SecEvalBase.json | tee /home/melissa/sven/scripts/codeseceval_student.txt

# Inverse dataset
python /home/melissa/sven/scripts/all_analyzers.py /home/melissa/sven/experiments/sec_eval/SecEval_Inverse_Analysis/trained/new_dataset /home/melissa/CodeSecEval-Inverse/SecEvalBase/SecEvalBase.json | tee /home/melissa/sven/scripts/codeseceval_inverse.txt

# Plus dataset
python /home/melissa/sven/scripts/all_analyzers.py /home/melissa/sven/experiments/sec_eval/SecEval_Plus_Analysis/trained/new_dataset /home/melissa/CodeSecEval/SecEvalPlus/SecEvalPlus.json | tee /home/melissa/sven/scripts/codeseceval_plus.txt
