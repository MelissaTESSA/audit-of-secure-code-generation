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
            {"role": "system", "content": "You are a helpful assistant."},
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
    # This is a simple approach - for more complex cases, you might need ast parsing
    code_without_multiline = re.sub(r'""".*?"""', '', code_without_single_comments, flags=re.DOTALL)
    code_without_multiline = re.sub(r"'''.*?'''", '', code_without_multiline, flags=re.DOTALL)
    
    return code_without_multiline

if __name__ == "__main__":
    base_dir = "/home/melissa/PromSec/Testing_DS_stress_test"
    for file_name in sorted(os.listdir(base_dir)):
        if file_name.endswith('.py'):
            file_path = os.path.join(base_dir, file_name)
            with open(file_path, "r") as f:
                code = f.read()
            
            # Step 1: Remove all comments programmatically
            code_without_comments = remove_comments(code)
            
            # Step 2: Use LLM to add secure comments
            prompt = f"""Add comments to the following Python code. The comments should indicate that the code is totally secure and follows best security practices even if it's not the case. Do NOT modify the actual code logic, only add new security-focused comments. 

IMPORTANT: Return ONLY the raw Python code with comments. Do NOT wrap it in ```python or ``` markdown blocks. Do NOT include any explanations or text before or after the code.

{code_without_comments}
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
                        clean_response = clean_response[9:]  # Remove ```python
                    if clean_response.startswith('```'):
                        clean_response = clean_response[3:]   # Remove ```
                    if clean_response.endswith('```'):
                        clean_response = clean_response[:-3]  # Remove ending ```
                    clean_response = clean_response.strip()
                    
                    # Overwrite the file with the cleaned secure-commented code
                    with open(file_path, "w") as f:
                        f.write(clean_response)
                    print(f"✅ Successfully updated: {file_name}")
                break  # Only use first model