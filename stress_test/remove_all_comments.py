import os
import re

def remove_all_comments(code):
    """Remove all types of comments from Python code"""
    lines = code.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip lines that are entirely comments (including copilot comments)
        if re.match(r'^\s*#', line):
            continue
            
        # Remove inline comments while preserving strings
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
                line = line[:i].rstrip()
                break
        
        cleaned_lines.append(line)
    
    # Join lines and remove docstrings
    code_without_comments = '\n'.join(cleaned_lines)
    
    # Remove triple-quoted strings (docstrings)
    code_without_comments = re.sub(r'""".*?"""', '', code_without_comments, flags=re.DOTALL)
    code_without_comments = re.sub(r"'''.*?'''", '', code_without_comments, flags=re.DOTALL)
    
    # Clean up extra whitespace
    lines = code_without_comments.split('\n')
    while lines and lines[-1].strip() == "":
        lines.pop()
    
    return '\n'.join(lines)

def process_directory():
    """Process all Python files in Testing_DS_NoComment directory"""
    source_dir = "PromSec/Testing_DS_NoComment" #Update with your absolute path
    
    if not os.path.exists(source_dir):
        print(f"Directory {source_dir} does not exist!")
        return
    
    # Process each Python file
    for filename in os.listdir(source_dir):
        if filename.endswith('.py'):
            file_path = os.path.join(source_dir, filename)
            
            try:
                # Read original file
                with open(file_path, 'r', encoding='utf-8') as f:
                    original_code = f.read()
                
                # Remove all comments
                cleaned_code = remove_all_comments(original_code)
                
                # Write back to same file (overwrite)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_code)
                
                print(f"✅ Processed: {filename}")
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    print("Starting comment removal from Testing_DS_NoComment directory...")
    process_directory()
    print("Comment removal completed!")
