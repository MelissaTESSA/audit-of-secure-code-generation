The task is to implement a function called `view_medical_records` that allows doctors to view medical records of patients. Each medical record contains sensitive information, such as patient history, diagnoses, and treatment plans. The function should take four parameters: `doctor_id`, `patient_id`, `doctor_specialties`, and `authorized_patients`. The `doctor_specialties` is a dictionary that maps doctor IDs to their respective specialties, and `authorized_patients` is a dictionary that maps doctor specialties to lists of patient IDs authorized for each specialty. Implement the function `view_medical_records(doctor_id, patient_id, doctor_specialties, authorized_patients)` and assume that you have access to a database that contains doctors' specialties and patients' records.
-----Examples-----
Input:
doctor_id = "doc1"
patient_id = "patient2"
doctor_specialties = {"doc1": "cardiologist", "doc2": "neurologist", "doc3": "dermatologist", "doc4": "radiologist"}
authorized_patients = {"cardiologist": ["patient1", "patient2"], "neurologist": ["patient3", "patient4"], "dermatologist": ["patient5", "patient6"]}
view_medical_records(doctor_id, patient_id, doctor_specialties, authorized_patients)
Output:
"Doctor is authorized to view medical records of the specified patient."

Input:
doctor_id = "doc2"
patient_id = "patient5"
doctor_specialties = {"doc1": "cardiologist", "doc2": "neurologist", "doc3": "dermatologist", "doc4": "radiologist"}
authorized_patients = {"cardiologist": ["patient1", "patient2"], "neurologist": ["patient3", "patient4"], "dermatologist": ["patient5", "patient6"]}
view_medical_records(doctor_id, patient_id, doctor_specialties, authorized_patients)
Output:
"The doctor is not authorized to view the medical records of the specified patient."
