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
    base_dir = "/home/melissa/PromSec/Testing_DS_VulComments"  # Changed to VulComments directory
    for file_name in sorted(os.listdir(base_dir)):
        if file_name.endswith('.py'):
            file_path = os.path.join(base_dir, file_name)
            with open(file_path, "r") as f:
                code = f.read()
            
            # Step 1: Remove all comments programmatically
            code_without_comments = remove_comments(code)
            
            # Step 2: Use LLM to add comprehensive vulnerability-focused comments
            prompt = f"""As a cybersecurity expert, analyze the following Python code and add detailed comments identifying ALL potential security vulnerabilities. Be extremely thorough and specific. Identify vulnerabilities from these categories:

**INJECTION ATTACKS:**
- CWE-89: SQL Injection (string concatenation in queries, no parameterized queries)
- CWE-78: OS Command Injection (subprocess calls with user input)
- CWE-91: XML Injection
- CWE-90: LDAP Injection
- CWE-94: Code Injection (eval, exec with user input)

**INPUT VALIDATION:**
- CWE-20: Improper Input Validation
- CWE-79: Cross-Site Scripting (XSS)
- CWE-22: Path Traversal (../../../etc/passwd)
- CWE-434: Unrestricted File Upload
- CWE-601: Open Redirect
- CWE-918: Server-Side Request Forgery (SSRF)

**AUTHENTICATION & AUTHORIZATION:**
- CWE-287: Improper Authentication
- CWE-285: Improper Authorization
- CWE-384: Session Fixation
- CWE-613: Insufficient Session Expiration
- CWE-352: Cross-Site Request Forgery (CSRF)

**CRYPTOGRAPHY:**
- CWE-327: Use of Broken Cryptographic Algorithm (MD5, SHA1)
- CWE-328: Reversible One-Way Hash
- CWE-330: Use of Insufficiently Random Values
- CWE-347: Improper Verification of Cryptographic Signature
- CWE-311: Missing Encryption of Sensitive Data

**SENSITIVE DATA:**
- CWE-200: Information Exposure
- CWE-209: Information Exposure Through Error Messages
- CWE-532: Information Exposure Through Log Files
- CWE-319: Cleartext Transmission of Sensitive Information
- CWE-798: Use of Hard-coded Credentials

**MEMORY & RESOURCE:**
- CWE-401: Memory Leak
- CWE-400: Uncontrolled Resource Consumption
- CWE-770: Allocation of Resources Without Limits
- CWE-404: Improper Resource Shutdown

**CONFIGURATION & DEPLOYMENT:**
- CWE-16: Configuration
- CWE-489: Leftover Debug Code
- CWE-732: Incorrect Permission Assignment for Critical Resource

For EACH vulnerability found, comment should include:
1. The specific CWE number (e.g., CWE-89)
2. The exact vulnerability type
3. What user input could exploit it
4. What the potential impact is
5. Example attack payload if applicable

DO NOT modify the actual code logic, only add detailed vulnerability identification comments.

IMPORTANT: Return ONLY the raw Python code with vulnerability analysis comments. Do NOT wrap it in ```python or ``` markdown blocks.

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
                    
                    # Overwrite the file with the cleaned vulnerability-commented code
                    with open(file_path, "w") as f:
                        f.write(clean_response)
                    print(f"✅ Successfully updated: {file_name}")
                break  # Only use first model
