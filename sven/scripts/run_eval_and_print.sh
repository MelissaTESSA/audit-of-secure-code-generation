#!/bin/bash

# Script to run sec_eval.py and print_results.py for different model prefixes and data directories
# Each block below runs evaluation and prints results for a specific model and data variant

# 2b-prefix on trained_append_10lines
python sec_eval.py --model_type prefix --model_dir ../trained/2b-prefix/checkpoint-last --output_name sec-eval-2b-prefix --data_dir ../data_eval/trained_append_10lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-2b-prefix

# 2b-prefix on trained_insert_10lines_strategic
python sec_eval.py --model_type prefix --model_dir ../trained/2b-prefix/checkpoint-last --output_name sec-eval-2b-prefix --data_dir ../data_eval/trained_insert_10lines_strategic
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-2b-prefix

# 2b-prefix on trained_append_200lines_functions
python sec_eval.py --model_type prefix --model_dir ../trained/2b-prefix/checkpoint-last --output_name sec-eval-2b-prefix --data_dir ../data_eval/trained_append_200lines_functions
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-2b-prefix

# 2b-prefix on trained_append_50lines
python sec_eval.py --model_type prefix --model_dir ../trained/2b-prefix/checkpoint-last --output_name sec-eval-2b-prefix --data_dir ../data_eval/trained_append_50lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-2b-prefix

# 350m-prefix on trained_append_10lines
python sec_eval.py --model_type prefix --model_dir ../trained/350m-prefix/checkpoint-last --output_name sec-eval-350m-prefix --data_dir ../data_eval/trained_append_10lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-350m-prefix

# 350m-prefix on trained_insert_10lines_strategic
python sec_eval.py --model_type prefix --model_dir ../trained/350m-prefix/checkpoint-last --output_name sec-eval-350m-prefix --data_dir ../data_eval/trained_insert_10lines_strategic
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-350m-prefix

# 350m-prefix on trained_append_200lines_functions
python sec_eval.py --model_type prefix --model_dir ../trained/350m-prefix/checkpoint-last --output_name sec-eval-350m-prefix --data_dir ../data_eval/trained_append_200lines_functions
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-350m-prefix

# 350m-prefix on trained_append_50lines
python sec_eval.py --model_type prefix --model_dir ../trained/350m-prefix/checkpoint-last --output_name sec-eval-350m-prefix --data_dir ../data_eval/trained_append_50lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-350m-prefix

# 6b-prefix on trained_append_10lines
python sec_eval.py --model_type prefix --model_dir ../trained/6b-prefix/checkpoint-last --output_name sec-eval-6b-prefix --data_dir ../data_eval/trained_append_10lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-6b-prefix

# 6b-prefix on trained_insert_10lines_strategic
python sec_eval.py --model_type prefix --model_dir ../trained/6b-prefix/checkpoint-last --output_name sec-eval-6b-prefix --data_dir ../data_eval/trained_insert_10lines_strategic
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-6b-prefix

# 6b-prefix on trained_append_200lines_functions
python sec_eval.py --model_type prefix --model_dir ../trained/6b-prefix/checkpoint-last --output_name sec-eval-6b-prefix --data_dir ../data_eval/trained_append_200lines_functions
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-6b-prefix

# 6b-prefix on trained_append_50lines
python sec_eval.py --model_type prefix --model_dir ../trained/6b-prefix/checkpoint-last --output_name sec-eval-6b-prefix --data_dir ../data_eval/trained_append_50lines
python print_results.py --eval_dir ../experiments/sec_eval/sec-eval-6b-prefix
