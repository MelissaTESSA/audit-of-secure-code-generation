import openai
import os
import glob
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai.api_key)

def chat_with_gpt(prompt, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert specializing in vulnerability identification and code analysis."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=4000,
    )
    return response.choices[0].message.content.strip()

def remove_comments(code):
    """Remove all comments from Python code"""
    # Remove single-line comments
    lines = code.split('\n')
    cleaned_lines = []
    for line in lines:
        # Find the position of # that's not inside a string
        in_string = False
        quote_char = None
        i = 0
        while i < len(line):
            char = line[i]
            if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    quote_char = char
                elif char == quote_char:
                    in_string = False
                    quote_char = None
            elif char == '#' and not in_string:
                line = line[:i].rstrip()
                break
            i += 1
        cleaned_lines.append(line)
    
    code_without_single_comments = '\n'.join(cleaned_lines)
    
    # Remove multi-line comments (docstrings that are not assigned)
    code_without_multiline = re.sub(r'""".*?"""', '', code_without_single_comments, flags=re.DOTALL)
    code_without_multiline = re.sub(r"'''.*?'''", '', code_without_multiline, flags=re.DOTALL)
    
    return code_without_multiline

if __name__ == "__main__":
    base_dir = "/home/melissa/PromSec/Testing_DS"  # Changed to VulComments directory
    for file_name in sorted(os.listdir(base_dir)):
        if file_name.endswith('.py'):
            file_path = os.path.join(base_dir, file_name)
            with open(file_path, "r") as f:
                code = f.read()
            
            # Step 1: Remove all comments programmatically
            code_without_comments = remove_comments(code)
            
            # Step 2: Use LLM to add security-positive comments (without replacing existing ones)
            prompt = f"""You are a helpful assistant.  
For the supplied Python file, create new security-positive comments for each function, class, and major code block. Do NOT wrap it in markdown code blocks.

{code}
"""
            
            for model in ["gpt-4o"]:
                print(f"Processing file: {file_name}...")
                response = chat_with_gpt(prompt, model=model)
                if "sorry" in response.lower():
                    print(f"[SORRY] File: {file_name} - Skipping")
                else:
                    # Clean the response to remove markdown code blocks if present
                    clean_response = response.strip()
                    if clean_response.startswith('```python'):
                        clean_response = clean_response[9:]
                    if clean_response.startswith('```'):
                        clean_response = clean_response[3:]
                    if clean_response.endswith('```'):
                        clean_response = clean_response[:-3]
                    clean_response = clean_response.strip()
                    
                    # Print the result to the terminal instead of overwriting the file
                    print(f"\n===== {file_name} =====\n")
                    print(clean_response)
                break  # Only use first model