import openai
import os

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
    result = response.choices[0].message.content.strip()
    # Remove markdown code blocks if present
    if result.startswith('```python'):
        result = result[9:]
    if result.startswith('```'):
        result = result[3:]
    if result.endswith('```'):
        result = result[:-3]
    return result.strip()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

if __name__ == "__main__":
    base_dir = "PromSec/Testing_DS_examples" #Update with your absolute path
    for file_name in sorted(os.listdir(base_dir)):
        if file_name.endswith('.py'):
            file_path = os.path.join(base_dir, file_name)
            with open(file_path, "r") as f:
                code = f.read()
            prompt = f"""Return the entire following Python code unchanged, and append a single example as a Python docstring (triple quotes) at the end. The example should start with: -----Examples----- and include one sample input and output, similar to:\n\nReads the XML from the incoming request. Parse it and return.\n\n-----Examples-----\nInput:\nAn HTTP POST request with XML data\nupload()\nOutput:\n(No output, XML parsed and returned)\n\nDo NOT modify the code logic, only append this example as a docstring at the end. IMPORTANT: Return ONLY the full original Python code with the single example as a docstring at the end. Do NOT wrap it in markdown blocks.\n\n{code}\n"""
            print(f"\n===== {file_name} =====\n")
            response = chat_with_gpt(prompt, model="gpt-4o")
            print(response)
            with open(file_path, "w") as f:
                f.write(response)

