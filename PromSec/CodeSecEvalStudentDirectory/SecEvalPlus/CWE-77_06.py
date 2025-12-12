Implement a function `rename_file(old_name, new_name)` that takes the current file name and the new file name as inputs. This function constructs a shell command to rename a file using these inputs and executes it. The function should return a confirmation message if the operation is successful or an error message if it fails due to security concerns or invalid input.

This function is intended for use in applications requiring file management capabilities, allowing users to rename files dynamically based on input.

-----Examples-----
Input:
old_name = "report.txt"
new_name = "updated_report.txt"
rename_file(old_name, new_name)
Output:
"File renamed successfully: updated_report.txt"
