#!/usr/bin/env python3
"""
Stress Test - Comment to Question
Removes all comments except the last one, then converts the last comment into a simple student question.
"""

import os
import re
import openai

BASE_DIR = "/home/melissa/sven/data_eval/train_CommentToQuestion/trained"
MODEL = "gpt-4o"

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", "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")
client = openai.OpenAI(api_key=openai.api_key)

def get_openai_response(prompt, model=MODEL):
    """Get response from OpenAI API."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"  ✗ OpenAI API error: {e}")
        return None

def extract_comments(content):
    """Extract all comment lines from the content."""
    lines = content.split('\n')
    comments = []
    
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        # Check for Python or C/C++ comments
        if stripped.startswith('#'):
            comments.append((i, line, 'python'))
        elif stripped.startswith('//'):
            comments.append((i, line, 'c'))
    
    return comments

def convert_comment_to_question(comment_text, language, code_context):
    """Convert a comment into a simple student question using GPT."""
    # Remove comment markers
    if language == 'python':
        comment_text = comment_text.lstrip().lstrip('#').strip()
    else:  # C/C++
        comment_text = comment_text.lstrip().lstrip('//').strip()
    
    prompt = f"""You are helping convert a code comment into a simple, natural question that a student would ask.

Original comment: \"{comment_text}\"

Context (code snippet):
{code_context[:300]}...

Convert this comment into a short, simple question (1 sentence) that a student learning to code would ask. 
The question should be natural and conversational, like \"how do I...\" or \"what should I do to...\".
Keep it brief and clear. Respond with ONLY the question, no quotes or extra text."""

    response = get_openai_response(prompt)
    return response if response else comment_text

def process_file(file_path):
    """Keep only the last comment in the file, convert it to a student question."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        comments = extract_comments(content)
        
        if len(comments) == 0:
            print(f"  ⚠ {file_path}: No comments found")
            return False
        
        if len(comments) == 1:
            # Only one comment, convert it to question
            idx, comment_line, lang = comments[0]
            print(f"  → Converting single comment to question...")
            question = convert_comment_to_question(comment_line, lang, content)
            if question:
                # Replace the comment with the question
                indent = len(comment_line) - len(comment_line.lstrip())
                if lang == 'python':
                    new_comment = ' ' * indent + f"# {question}"
                else:
                    new_comment = ' ' * indent + f"// {question}"
                lines[idx] = new_comment
                new_content = '\n'.join(lines)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ✓ {file_path}: Converted 1 comment to question")
                return True
            return False
        
        # Multiple comments: remove all except last, then convert last to question
        last_idx, last_comment, last_lang = comments[-1]
        lines_to_remove = [idx for idx, _, _ in comments[:-1]]  # All except last
        
        print(f"  → Removing {len(comments)-1} comment(s), converting last to question...")
        
        # Convert last comment to question
        question = convert_comment_to_question(last_comment, last_lang, content)
        if question:
            # Replace last comment with question
            indent = len(last_comment) - len(last_comment.lstrip())
            if last_lang == 'python':
                new_last_comment = ' ' * indent + f"# {question}"
            else:
                new_last_comment = ' ' * indent + f"// {question}"
            lines[last_idx] = new_last_comment
        
        # Create new content without the removed comment lines
        new_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
        new_content = '\n'.join(new_lines)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ {file_path}: Removed {len(comments)-1} comment(s), converted last to question")
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
                    if process_file(func_context_path):
                        modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Processing complete!")
    print(f"   Total files processed: {total_files}")
    print(f"   Files modified: {modified_count}")
    print(f"   Files unchanged: {total_files - modified_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("="*60)
    print("🔧 Stress Test - Comment to Question")
    print("="*60)
    print(f"Dataset: {BASE_DIR}")
    print("Action: Keep only last comment, convert to student question")
    print(f"Model: {MODEL}")
    print("="*60)
    
    if not openai.api_key or openai.api_key == "your-api-key-here":
        print("\n⚠️  WARNING: OpenAI API key not set!")
        print("   Set OPENAI_API_KEY environment variable or update the script.")
        exit(1)
    
    process_dataset()
