#!/bin/bash

# SafeCoder Evaluation Script for Multiple Datasets
# Runs codellama-7b-lora-safecoder on trained, train_stress_test, and train_stress_test_student

set -e  # Exit on error

# Configuration
MODEL_NAME="codellama-7b-lora-safecoder"
OUTPUT_BASE="codellama-7b-safecoder"
DATASETS=("trained" "train_stress_test" "train_stress_test_student")
NUM_SAMPLES=100
NUM_SAMPLES_PER_GEN=20
TEMP=0.4
MAX_GEN_LEN=256
TOP_P=0.95
# Empty VUL_TYPE means run all CWEs
VUL_TYPE=""

# Create output directory with timestamp (absolute path)
OUTPUT_DIR="/home/melissa/SafeCoder/all_outputs_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTPUT_DIR"

# Summary file for all results
SUMMARY_FILE="${OUTPUT_DIR}/all_results_summary.txt"
echo "=== SAFECODER SECURITY EVALUATION RESULTS ===" > "$SUMMARY_FILE"
echo "Generated on: $(date)" >> "$SUMMARY_FILE"
echo "Model: $MODEL_NAME" >> "$SUMMARY_FILE"
echo "Parameters: num_samples=$NUM_SAMPLES, temp=$TEMP, max_gen_len=$MAX_GEN_LEN" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# Activate virtual environment
source safecoder_env/bin/activate

# Set environment variables
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export PYTHONPATH=/home/melissa/SafeCoder

echo "🚀 Starting SafeCoder evaluations..."
echo ""

for dataset in "${DATASETS[@]}"; do
  echo "========================================" | tee -a "$SUMMARY_FILE"
  echo "📊 Running evaluation on dataset: $dataset" | tee -a "$SUMMARY_FILE"
  echo "========================================" | tee -a "$SUMMARY_FILE"
  
  # Create combined output file for this dataset
  combined_file="${OUTPUT_DIR}/results_${dataset}.txt"
  
  # Initialize combined file with header
  echo "=== SAFECODER EVALUATION: $dataset ===" > "$combined_file"
  echo "Generated on: $(date)" >> "$combined_file"
  echo "Model: $MODEL_NAME" >> "$combined_file"
  echo "" >> "$combined_file"
  
  # Run the evaluation from scripts directory
  cd /home/melissa/SafeCoder/scripts
  
  echo "▶️  Running sec_eval.py..." | tee -a "$SUMMARY_FILE"
  
  # sec_eval.py does: args.data_dir = os.path.join(args.data_dir, args.eval_type)
  # For stress test datasets, create a temp symlink so path resolves correctly
  if [ "$dataset" = "trained" ]; then
    DATA_DIR_ARG="/home/melissa/SafeCoder/data_eval/sec_eval"
  else
    TEMP_PARENT="/home/melissa/SafeCoder/data_eval/temp_${dataset}"
    mkdir -p "$TEMP_PARENT"
    rm -f "${TEMP_PARENT}/trained"
    ln -s "/home/melissa/SafeCoder/data_eval/sec_eval/${dataset}" "${TEMP_PARENT}/trained"
    DATA_DIR_ARG="$TEMP_PARENT"
  fi
  
  # Run evaluation and capture exit code properly
  set +e  # Temporarily disable exit on error to capture the actual result
  python sec_eval.py \
    --output_name "${OUTPUT_BASE}_${dataset}" \
    --model_name "$MODEL_NAME" \
    --eval_type "trained" \
    --num_samples "$NUM_SAMPLES" \
    --num_samples_per_gen "$NUM_SAMPLES_PER_GEN" \
    --temp "$TEMP" \
    --max_gen_len "$MAX_GEN_LEN" \
    --top_p "$TOP_P" \
    --vul_type "$VUL_TYPE" \
    --experiments_dir /home/melissa/SafeCoder/experiments \
    --data_dir "$DATA_DIR_ARG" \
    --model_dir /home/melissa/SafeCoder \
    2>&1 | tee -a "$combined_file"
  
  EVAL_EXIT_CODE=${PIPESTATUS[0]}
  set -e  # Re-enable exit on error
  
  # Check if evaluation succeeded
  if [ $EVAL_EXIT_CODE -eq 0 ]; then
    echo "✅ Evaluation completed successfully for $dataset" | tee -a "$SUMMARY_FILE"
    
    # Only use print_results.py if we ran all vulnerabilities (no vul_type specified)
    if [ -z "$VUL_TYPE" ]; then
      # Use print_results.py for nicely formatted output
      echo "📈 Generating results summary..." | tee -a "$SUMMARY_FILE"
      
      # Add separator to combined file
      echo "" >> "$combined_file"
      echo "=== FORMATTED RESULTS ===" >> "$combined_file"
      echo "" >> "$combined_file"
      
      # Run print_results.py and capture output
      python print_results.py \
        --eval_name "${OUTPUT_BASE}_${dataset}" \
        --eval_type "trained" \
        --experiments_dir /home/melissa/SafeCoder/experiments \
        2>&1 | tee -a "$combined_file" | tee -a "$SUMMARY_FILE"
      
      if [ ${PIPESTATUS[0]} -eq 0 ]; then
        echo "" | tee -a "$SUMMARY_FILE"
        echo "✅ Results printed successfully for $dataset" | tee -a "$SUMMARY_FILE"
      else
        echo "⚠️  Warning: print_results.py failed, using fallback" | tee -a "$SUMMARY_FILE"
      fi
    else
      echo "📈 Results for ${VUL_TYPE} (from sec_eval.py output above)" | tee -a "$SUMMARY_FILE"
      echo "" | tee -a "$SUMMARY_FILE"
    fi
  else
    echo "❌ Evaluation failed for $dataset" | tee -a "$SUMMARY_FILE"
    echo "Check log: $combined_file" | tee -a "$SUMMARY_FILE"
  fi
  
  # Cleanup temporary directory structure AFTER everything is done
  if [ "$dataset" != "trained" ]; then
    rm -rf "$TEMP_PARENT"
  fi
  
  echo "" >> "$SUMMARY_FILE"
  echo ""
done

# Return to SafeCoder root directory
cd /home/melissa/SafeCoder

echo "========================================" | tee -a "$SUMMARY_FILE"
echo "🎉 All evaluations completed!" | tee -a "$SUMMARY_FILE"
echo "📁 Results summary: $OUTPUT_DIR/$SUMMARY_FILE" | tee -a "$SUMMARY_FILE"
echo "📁 Individual logs: $OUTPUT_DIR/" | tee -a "$SUMMARY_FILE"
echo "========================================" | tee -a "$SUMMARY_FILE"

# Print final summary location
echo ""
echo "✅ Complete! Check these files for results:"
echo "   - Summary: $OUTPUT_DIR/$(basename $SUMMARY_FILE)"
for dataset in "${DATASETS[@]}"; do
  echo "   - $dataset: $OUTPUT_DIR/results_${dataset}.txt"
done
echo ""
