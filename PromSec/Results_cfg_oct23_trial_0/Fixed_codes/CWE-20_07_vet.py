import os

def process_patient_record(patient_data):
    name = patient_data.get('name', '')
    age = patient_data.get('age', '')
    blood_type = patient_data.get('blood_type', '')
    conditions = patient_data.get('conditions', [])
    num_conditions = len(conditions)
    
    return f'Patient: {name}, Age: {age}, Blood Type: {blood_type}, Conditions: {num_conditions}'