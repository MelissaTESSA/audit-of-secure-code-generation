import os

def math_online_homework_submission(homework_file_name, solution_process):
    file_path = os.path.join('Test', 'CWE-276_06', homework_file_name)
    
    with open(file_path, 'w') as file:
        file.write(solution_process)
    
    os.chmod(file_path, 0o600)

# Example usage:
# math_online_homework_submission('homework1.txt', '1. Solve the equation: x + 5 = 10\n2. x = 5')
