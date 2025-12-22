import openai
import os
import random
import string

def random_var_name(length=12):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

def generate_dead_code_lines(var_name, num_lines=10):
    prompt = f"""
Generate {num_lines} lines of Python dead code. All lines should be encapsulated inside a single variable named '{var_name}' as a multi-line string. The variable must not be used anywhere else. The dead code should look realistic (e.g., unused functions, assignments, control structures) but must not affect the rest of the code. Return only the Python code, no explanations or markdown.
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
    src_dir = "sven/data_eval/trained_append_10lines" #Update with your absolute path
    for cwe_dir in sorted(os.listdir(src_dir)):
        cwe_path = os.path.join(src_dir, cwe_dir)
        if os.path.isdir(cwe_path):
            for sub_dir in sorted(os.listdir(cwe_path)):
                sub_path = os.path.join(cwe_path, sub_dir)
                if os.path.isdir(sub_path):
                    for code_file in [os.path.join(sub_path, "func_context.py"), os.path.join(sub_path, "func_context.c")]:
                        if os.path.isfile(code_file):
                            with open(code_file, "r") as f:
                                original_code = f.read()
                            var_name = random_var_name()
                            dead_code = generate_dead_code_lines(var_name, num_lines=10)
                            new_code = original_code + "\n" + dead_code
                            with open(code_file, "w") as f:
                                f.write(new_code)
                            print(f"✅ Dead code appended to: {code_file}")
