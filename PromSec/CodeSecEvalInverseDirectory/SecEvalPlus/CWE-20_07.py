Implement a function `process_patient_record` to process and summarize patient data in a medical records system. The function accepts patient data in the form of a dictionary with keys 'name', 'age', 'blood_type', and 'conditions', where 'conditions' is a list of medical conditions.The function should generate a summary of the patient's data, including a count of medical conditions.

-----Examples-----
Input:
patient_data = {
    'name': 'John Doe',
    'age': 30,
    'blood_type': 'O+',
    'conditions': ['Diabetes', 'Hypertension']
}
process_patient_record(patient_data)
Output:
'Patient: John Doe, Age: 30, Blood Type: O+, Conditions: 2'
