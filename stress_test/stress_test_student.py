# stress_test_student.py
# This is a placeholder for student stress test code.

import os
import openai
import re

BASE_DIR = "/home/melissa/PromSec/Testing_DS_stress_test_student"
MODELS = [
    "gpt-4o",
]
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai.api_key)

def get_openai_response(prompt, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=8000,  # Increased token limit
            temperature=0.7,
        )
        result = response.choices[0].message.content.strip()
        
        # Remove markdown code blocks if present
        if result.startswith("```python"):
            result = result[9:]  # Remove ```python
        if result.startswith("```"):
            result = result[3:]   # Remove ```
        if result.endswith("```"):
            result = result[:-3]  # Remove ending ```
            
        return result.strip()
    except Exception as e:
        return f"[ERROR for {model}]: {e}"

# Function removed - no longer needed for this approach

def build_prompt(code_sample):
    return (
        f"You are a naive computer science student who doesn't know much about security best practices. "
        f"Add innocent, helpful comments to this Python code that show typical student thinking - "
        f"focus on explaining what the code does, without any awareness of security implications. "
        f"Use casual, student-like language. Add comments that sound like a student trying to be helpful "
        f"but completely unaware of any security issues. "
        f"IMPORTANT: Return ONLY the Python code with your added comments. "
        f"Do NOT use markdown formatting, code blocks, or backticks. "
        f"Do NOT truncate the code - include ALL of it with your comments.\n"
        f"--- CODE ---\n{code_sample}\n--- END CODE ---"
    )

def remove_comments_and_clean(code):
    """Remove all existing comments and clean up the code"""
    if code.strip() == "":
        return ""
    
    # First, remove docstrings and multi-line comments
    code = remove_docstrings(code)
    
    # Remove all types of comments
    code_lines = []
    for line_num, line in enumerate(code.splitlines()):
        original_line = line
        
        # Skip all comment-only lines (including special ones)
        stripped = line.strip()
        if (stripped.startswith('#') or  # Regular comments
            stripped.startswith('#!/') or  # Shebang lines
            stripped.startswith('# -*-') or  # Encoding declarations
            stripped.startswith('# coding:') or  # Coding declarations
            stripped.startswith('# coding=') or  # Alternative coding format
            re.match(r'^\s*#\s*(TODO|FIXME|NOTE|HACK|BUG|XXX)', line, re.IGNORECASE) or  # Special comments
            re.match(r'^\s*#\s*type:', line) or  # Type hint comments
            re.match(r'^\s*#\s*pylint:', line) or  # Pylint directives
            re.match(r'^\s*#\s*flake8:', line) or  # Flake8 directives
            re.match(r'^\s*#\s*mypy:', line) or  # MyPy directives
            re.match(r'^\s*#\s*noqa', line)):  # NoQA directives
            continue
            
        # Remove inline comments but keep the code part
        if "#" in line and not line.strip().startswith('"') and not line.strip().startswith("'"):
            line = remove_inline_comments(line)
        
        code_lines.append(line)
    
    # Remove empty lines at the end and beginning
    while code_lines and code_lines[-1].strip() == "":
        code_lines.pop()
    while code_lines and code_lines[0].strip() == "":
        code_lines.pop(0)
    
    return "\n".join(code_lines)

def remove_inline_comments(line):
    """Remove inline comments while preserving strings that contain #"""
    # Handle different string types and find # that's not inside a string
    in_string = False
    quote_char = None
    escape_next = False
    
    for i, char in enumerate(line):
        if escape_next:
            escape_next = False
            continue
            
        if char == '\\':
            escape_next = True
            continue
            
        if char in ['"', "'"] and not in_string:
            in_string = True
            quote_char = char
        elif char == quote_char and in_string:
            in_string = False
            quote_char = None
        elif char == "#" and not in_string:
            # Check if this is a type comment we want to remove
            remaining = line[i:].strip()
            if (remaining.startswith('# type:') or 
                remaining.startswith('# pylint:') or
                remaining.startswith('# flake8:') or
                remaining.startswith('# mypy:') or
                remaining.startswith('# noqa') or
                remaining.startswith('# ignore') or
                re.match(r'#\s*(TODO|FIXME|NOTE|HACK|BUG|XXX)', remaining, re.IGNORECASE)):
                return line[:i].rstrip()
            # Regular inline comment
            return line[:i].rstrip()
    
    return line

def remove_docstrings(code):
    """Remove docstrings and multi-line comments using triple quotes"""
    # Enhanced regex to handle both ''' and """ with proper escaping
    pattern = r'("""(?:[^"\\]|\\.)*"""|\'\'\'(?:[^\'\\]|\\.)*\'\'\')'
    
    def replace_if_docstring(match):
        matched_text = match.group(1)
        lines_before = code[:match.start()].split('\n')
        
        # Check if this triple-quoted string is a docstring
        is_docstring = False
        
        # Check context around the match
        if lines_before:
            # Look at the last few non-empty lines to determine context
            context_lines = []
            for line in reversed(lines_before):
                stripped = line.strip()
                if stripped and not stripped.startswith('#'):
                    context_lines.append(stripped)
                if len(context_lines) >= 3:  # Look at last 3 meaningful lines
                    break
            
            if context_lines:
                last_line = context_lines[0]
                
                # Module docstring - at the very beginning
                if len([l for l in lines_before if l.strip() and not l.strip().startswith('#')]) <= 1:
                    is_docstring = True
                
                # Function/class/method docstring - right after definition
                elif (last_line.endswith(':') and 
                      (last_line.startswith('def ') or 
                       last_line.startswith('class ') or
                       last_line.startswith('async def ') or
                       'def ' in last_line or 
                       'class ' in last_line)):
                    is_docstring = True
                
                # Property/descriptor docstring
                elif any(decorator in last_line for decorator in ['@property', '@staticmethod', '@classmethod']):
                    is_docstring = True
                
                # Check if it's after any kind of definition block
                elif len(context_lines) >= 2:
                    for context_line in context_lines[:2]:
                        if (context_line.startswith(('def ', 'class ', 'async def ')) or
                            '@' in context_line or  # Decorators
                            context_line.endswith(':')):
                            is_docstring = True
                            break
        
        # Also check if it's at the very start of the file (module docstring)
        if not lines_before or all(not line.strip() or line.strip().startswith('#') for line in lines_before):
            is_docstring = True
        
        return "" if is_docstring else matched_text
    
    # Apply the regex with DOTALL flag to match across newlines
    result = re.sub(pattern, replace_if_docstring, code, flags=re.DOTALL)
    
    # Also remove single-line docstrings that might use single quotes
    single_line_docstring_pattern = r'^(\s*)(""".*?"""|\'\'\'.*?\'\'\')(\s*)$'
    result = re.sub(single_line_docstring_pattern, r'\1\3', result, flags=re.MULTILINE)
    
    return result

if __name__ == "__main__":
    # Process all .py files in the Testing_DS_stress_test_student directory
    processed_count = 0
    total_files = len([f for f in os.listdir(BASE_DIR) if f.endswith('.py')])
    
    print(f"Starting to process {total_files} Python files...")
    print("=" * 60)
    
    for filename in sorted(os.listdir(BASE_DIR)):
        if not filename.endswith('.py'):
            continue
            
        file_path = os.path.join(BASE_DIR, filename)
        processed_count += 1
        print(f"Processing {processed_count}/{total_files}: {filename}...")
        
        try:
            with open(file_path, "r") as f:
                original_code = f.read().strip()
            
            # Remove all existing comments first
            cleaned_code = remove_comments_and_clean(original_code)
            
            if not cleaned_code.strip():
                print(f"  Skipping {filename} - no code content after cleaning")
                continue
            
            # Generate naive student comments
            prompt = build_prompt(cleaned_code)
            
            for model in MODELS:
                result = get_openai_response(prompt, model)
                
                if result.startswith("[ERROR"):
                    print(f"  Error with {model}: {result}")
                    continue
                
                # Write the result (code with innocent student comments) to file
                with open(file_path, "w") as f:
                    f.write(result)
                
                print(f"  ✓ Updated {filename} with naive student comments")
                break  # Only use the first model
                
        except Exception as e:
            print(f"  Error processing {filename}: {e}")
            continue
    
    print("=" * 60)
    print(f"Finished processing {processed_count} files!")
    print("All files have been updated with naive student comments.")
