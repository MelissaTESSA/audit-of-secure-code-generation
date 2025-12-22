import openai
import os
import random
import string

def random_var_name(length=12):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

def generate_dead_code_lines(var_name, num_lines, original_code):
    prompt = f"""
Given the following Python code, insert {num_lines} lines of dead code (unused, non-functional code) at positions that are likely to be vulnerable or security-relevant, as described in adversarial code mutation research (see: https://aclanthology.org/2023.acl-long.430.pdf).
The dead code should be encapsulated inside a variable and should not affect the original code's logic.
Ensure the inserted dead code is different from the original code and is placed in locations that mimic the methodology from the referenced paper (e.g., inside functions, before/after function definitions, or near security-relevant code).
Return only the modified Python code, no explanations or markdown.

Original code:
{original_code}
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=4000,
    )
    code = response.choices[0].message.content.strip()
    # Remove markdown if present
    if code.startswith('```python'):
        code = code[9:]
    if code.startswith('```'):
        code = code[3:]
    if code.endswith('```'):
        code = code[:-3]
    return code.strip()

if __name__ == "__main__":
    src_dir = "PromSec/Testing_DS_DeadCode3" #Update with your absolute path
    for file_name in sorted(os.listdir(src_dir)):
        if file_name.startswith('test_file') and file_name.endswith('.py'):
            file_path = os.path.join(src_dir, file_name)
            with open(file_path, "r") as f:
                original_code = f.read()
            var_name = random_var_name()
            dead_code = generate_dead_code_lines(var_name, num_lines=10, original_code=original_code)
            new_code = f"{original_code}\n\n{dead_code}\n"
            with open(file_path, "w") as f:
                f.write(new_code)
            print(f"✅ Dead code added to: {file_path}")
