#!/usr/bin/env python3
"""
Stress Test - One Comment Only
Removes all comments except the last one from func_context files in train_OneComment dataset.
"""

import os
import re

BASE_DIR = "/home/melissa/sven/data_eval/train_OneComment/trained"

def extract_comments(content):
    """Extract all comment lines from the content."""
    lines = content.split('\n')
    comments = []
    
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        # Check for Python or C/C++ comments
        if stripped.startswith('#') or stripped.startswith('//'):
            comments.append((i, line))
    
    return comments

def keep_only_last_comment(file_path):
    """Keep only the last comment in the file, remove all others."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        comments = extract_comments(content)
        
        if len(comments) <= 1:
            # 0 or 1 comment, nothing to change
            print(f"  ✓ {file_path}: {len(comments)} comment(s), no changes needed")
            return False
        
        # Remove all comments except the last one
        lines_to_remove = [idx for idx, _ in comments[:-1]]  # All except last
        
        # Create new content without the removed comment lines
        new_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
        new_content = '\n'.join(new_lines)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ {file_path}: Removed {len(comments)-1} comment(s), kept last one")
        return True
        
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")
        return False

def process_dataset():
    """Process all func_context files in the dataset."""
    modified_count = 0
    total_files = 0
    
    # Walk through all CWE directories
    for cwe_dir in sorted(os.listdir(BASE_DIR)):
        cwe_path = os.path.join(BASE_DIR, cwe_dir)
        if not os.path.isdir(cwe_path):
            continue
        
        print(f"\n📁 Processing {cwe_dir}...")
        
        # Walk through scenario directories
        for scenario_dir in sorted(os.listdir(cwe_path)):
            scenario_path = os.path.join(cwe_path, scenario_dir)
            if not os.path.isdir(scenario_path):
                continue
            
            # Process func_context files
            for filename in ['func_context.py', 'func_context.c']:
                func_context_path = os.path.join(scenario_path, filename)
                if os.path.exists(func_context_path):
                    total_files += 1
                    if keep_only_last_comment(func_context_path):
                        modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Processing complete!")
    print(f"   Total files processed: {total_files}")
    print(f"   Files modified: {modified_count}")
    print(f"   Files unchanged: {total_files - modified_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("="*60)
    print("🔧 Stress Test - One Comment Only")
    print("="*60)
    print(f"Dataset: {BASE_DIR}")
    print("Action: Remove all comments except the last one")
    print("="*60)
    
    process_dataset()
