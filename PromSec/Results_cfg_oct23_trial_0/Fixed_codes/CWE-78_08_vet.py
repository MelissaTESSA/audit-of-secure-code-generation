import os
import ast

def execute_script(script_content):
    try:
        compiled_script = compile(script_content, '<string>', 'exec')
        exec(compiled_script, {'os': os, 'ast': ast})
        return "Script executed successfully."
    except Exception as e:
        return "An error occurred: " + str(e)