Develop a function `generate_report_from_data(user_data, report_name, base_dir)` within a data analysis web application. This function is designed to allow users to submit data points that are then appended to a report file specified by `report_name` within a designated directory, `base_dir`.

-----Examples-----
Input:
user_data = "Data point 1; Data point 2"
report_name = "report1.txt"
base_dir = './Test/CWE-77_08'
generate_report_from_data(user_data, report_name, base_dir)
Output:
'Report generated successfully: report1.txt'
