
import os
import json

def json_to_py_files(json_path, output_dir):
    """
    Reads a JSON file containing a list of problems, and writes each problem to a .py file named by its ID.
    Assumes each entry in the JSON is a dict with 'ID' and 'Problem' fields.
    """
    os.makedirs(output_dir, exist_ok=True)
    with open(json_path, 'r') as f:
        data = json.load(f)
    # If the JSON is a dict with a list under a key, adjust as needed
    if isinstance(data, dict) and 'Problems' in data:
        problems = data['Problems']
    elif isinstance(data, list):
        problems = data
    else:
        problems = [data]
    for entry in problems:
        file_id = str(entry['ID']).replace('/', '_')  # Replace slashes with underscores
        problem_code = entry['Problem']
        file_path = os.path.join(output_dir, f"{file_id}.py")
        with open(file_path, 'w') as py_file:
            py_file.write(problem_code)
    print(f"Created {len(problems)} .py files in {output_dir}")

if __name__ == "__main__":

    
    # Student version - Base and Plus
    student_base_json = "CodeSecEval-Student/SecEvalBase/SecEvalBase.json"
    student_base_out = "CodeSecEvalStudentDirectory/SecEvalBase"
    
    student_plus_json = "CodeSecEval-Student/SecEvalPlus/SecEvalPlus.json"
    student_plus_out = "CodeSecEvalStudentDirectory/SecEvalPlus"
    
    # Inverse version - Base and Plus
    inverse_base_json = "CodeSecEval-Inverse/SecEvalBase/SecEvalBase.json"
    inverse_base_out = "CodeSecEvalInverseDirectory/SecEvalBase"
    
    inverse_plus_json = "CodeSecEval-Inverse/SecEvalPlus/SecEvalPlus.json"
    inverse_plus_out = "CodeSecEvalInverseDirectory/SecEvalPlus"
    
    # Process all versions
    # json_to_py_files(base_json, base_out)
    # json_to_py_files(plus_json, plus_out)
    json_to_py_files(student_base_json, student_base_out)
    json_to_py_files(student_plus_json, student_plus_out)
    json_to_py_files(inverse_base_json, inverse_base_out)
    json_to_py_files(inverse_plus_json, inverse_plus_out)
