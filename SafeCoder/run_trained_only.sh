#!/bin/bash

# ========================================
# SafeCoder Evaluation Script (ALL COMMENTED OUT)
# Datasets: trained_append_10lines, trained_append_50lines, trained_insert_10lines_strategic, trained_append_200lines_functions
# ========================================

# =====================
# trained_append_10lines
# =====================
#
# <EVALUATION BLOCK FOR trained_append_10lines GOES HERE>
#
# Example:
# cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_append_10lines /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines/trained && python sec_eval.py \
#   --output_name codellama-7b-safecoder_trained_append_10lines \
#   --model_name codellama-7b-lora-safecoder \
#   --eval_type trained \
#   --num_samples 100 \
#   --num_samples_per_gen 20 \
#   --experiments_dir /home/melissa/SafeCoder/experiments \
#   --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines \
#   --model_dir /home/melissa/SafeCoder \
#   2>&1 | tee -a "$OUTPUT_FILE"
#
# ...add result printing and cleanup as needed...

# =====================
# trained_append_50lines
# =====================
#
# <EVALUATION BLOCK FOR trained_append_50lines GOES HERE>
#
# Example:
# cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_append_50lines /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines/trained && python sec_eval.py \
#   --output_name codellama-7b-safecoder_trained_append_50lines \
#   --model_name codellama-7b-lora-safecoder \
#   --eval_type trained \
#   --num_samples 100 \
#   --num_samples_per_gen 20 \
#   --experiments_dir /home/melissa/SafeCoder/experiments \
#   --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines \
#   --model_dir /home/melissa/SafeCoder \
#   2>&1 | tee -a "$OUTPUT_FILE"
#
# ...add result printing and cleanup as needed...

# =====================
# trained_insert_10lines_strategic
# =====================
#
# <EVALUATION BLOCK FOR trained_insert_10lines_strategic GOES HERE>
#
# Example:
# cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_insert_10lines_strategic /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic/trained && python sec_eval.py \
#   --output_name codellama-7b-safecoder_trained_insert_10lines_strategic \
#   --model_name codellama-7b-lora-safecoder \
#   --eval_type trained \
#   --num_samples 100 \
#   --num_samples_per_gen 20 \
#   --experiments_dir /home/melissa/SafeCoder/experiments \
#   --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic \
#   --model_dir /home/melissa/SafeCoder \
#   2>&1 | tee -a "$OUTPUT_FILE"
#
# ...add result printing and cleanup as needed...

# =====================
# trained_append_200lines_functions
# =====================
#
# <EVALUATION BLOCK FOR trained_append_200lines_functions GOES HERE>
#
# Example:
# cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_append_200lines_functions /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions/trained && python sec_eval.py \
#   --output_name codellama-7b-safecoder_trained_append_200lines_functions \
#   --model_name codellama-7b-lora-safecoder \
#   --eval_type trained \
#   --num_samples 100 \
#   --num_samples_per_gen 20 \
#   --experiments_dir /home/melissa/SafeCoder/experiments \
#   --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions \
#   --model_dir /home/melissa/SafeCoder \
#   2>&1 | tee -a "$OUTPUT_FILE"
#
# ...add result printing and cleanup as needed...

# ========================================
# END OF SCRIPT (ALL COMMENTED)
# ========================================

# =====================
# Evaluation blocks for new datasets (READY TO RUN)
# =====================

echo "=== Running evaluation: trained_append_50lines ==="
cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_append_50lines /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines/trained && python sec_eval.py \
  --output_name codellama-7b-safecoder_trained_append_50lines \
  --model_name codellama-7b-lora-safecoder \
  --eval_type trained \
  --num_samples 100 \
  --num_samples_per_gen 20 \
  --experiments_dir /home/melissa/SafeCoder/experiments \
  --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_append_50lines \
  --model_dir /home/melissa/SafeCoder || true

# Check GPU memory and wait to help avoid OOM
nvidia-smi
sleep 10

echo "=== FORMATTED RESULTS: trained_append_50lines ==="
python print_results.py \
  --eval_name codellama-7b-safecoder_trained_append_50lines \
  --eval_type trained \
  --experiments_dir /home/melissa/SafeCoder/experiments || true

echo "=== Running evaluation: trained_insert_10lines_strategic ==="
cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_insert_10lines_strategic /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic/trained && python sec_eval.py \
  --output_name codellama-7b-safecoder_trained_insert_10lines_strategic \
  --model_name codellama-7b-lora-safecoder \
  --eval_type trained \
  --num_samples 100 \
  --num_samples_per_gen 20 \
  --experiments_dir /home/melissa/SafeCoder/experiments \
  --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_insert_10lines_strategic \
  --model_dir /home/melissa/SafeCoder || true

# Check GPU memory and wait to help avoid OOM
nvidia-smi
sleep 10

echo "=== FORMATTED RESULTS: trained_insert_10lines_strategic ==="
python print_results.py \
  --eval_name codellama-7b-safecoder_trained_insert_10lines_strategic \
  --eval_type trained \
  --experiments_dir /home/melissa/SafeCoder/experiments || true

echo "=== Running evaluation: trained_append_200lines_functions ==="
cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_append_200lines_functions /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions/trained && python sec_eval.py \
  --output_name codellama-7b-safecoder_trained_append_200lines_functions \
  --model_name codellama-7b-lora-safecoder \
  --eval_type trained \
  --num_samples 100 \
  --num_samples_per_gen 20 \
  --experiments_dir /home/melissa/SafeCoder/experiments \
  --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_append_200lines_functions \
  --model_dir /home/melissa/SafeCoder || true

# Check GPU memory and wait to help avoid OOM
nvidia-smi
sleep 10

echo "=== FORMATTED RESULTS: trained_append_200lines_functions ==="
python print_results.py \
  --eval_name codellama-7b-safecoder_trained_append_200lines_functions \
  --eval_type trained \
  --experiments_dir /home/melissa/SafeCoder/experiments || true



# trained_append_10lines
echo "=== Running evaluation: trained_append_10lines ==="
cd /home/melissa/SafeCoder/scripts && source ../safecoder_env/bin/activate && export PYTHONPATH=/home/melissa/SafeCoder && mkdir -p /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines && rm -f /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines/trained && ln -s /home/melissa/SafeCoder/data_eval/sec_eval/trained_append_10lines /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines/trained && python sec_eval.py \
  --output_name codellama-7b-safecoder_trained_append_10lines \
  --model_name codellama-7b-lora-safecoder \
  --eval_type trained \
  --num_samples 100 \
  --num_samples_per_gen 20 \
  --experiments_dir /home/melissa/SafeCoder/experiments \
  --data_dir /home/melissa/SafeCoder/data_eval/temp_trained_append_10lines \
  --model_dir /home/melissa/SafeCoder || true

# Check GPU memory and wait to help avoid OOM
nvidia-smi
sleep 10

echo "=== FORMATTED RESULTS: trained_append_10lines ==="
python print_results.py \
  --eval_name codellama-7b-safecoder_trained_append_10lines \
  --eval_type trained \
  --experiments_dir /home/melissa/SafeCoder/experiments || true
