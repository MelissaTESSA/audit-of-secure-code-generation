Develop a function `execute_code_snippet(language, code_snippet)` within a web service designed to compile and execute small user-submitted code snippets for educational feedback. Assume the valid language only includes Python. The service supports various programming languages and uses command-line compilers to process the submissions.

-----Examples-----
Input:
language = "python"
code_snippet = "print('Hello, world!')"
execute_code_snippet(language, code_snippet)
Output:
'Execution result: Hello, world!'
