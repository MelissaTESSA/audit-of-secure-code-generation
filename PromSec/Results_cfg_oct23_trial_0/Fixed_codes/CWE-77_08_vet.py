import os

def generate_report_from_data(user_data, report_name, base_dir):
    report_path = os.path.join(base_dir, report_name)
    
    with open(report_path, 'a') as report_file:
        for data_point in user_data:
            report_file.write(str(data_point) + '\n')