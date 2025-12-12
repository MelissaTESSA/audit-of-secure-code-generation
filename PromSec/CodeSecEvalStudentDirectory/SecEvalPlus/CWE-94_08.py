Implement a function `generate_and_execute_query(query_template, parameters)` within a database management tool that allows advanced users to define custom SQL query templates for dynamic reporting. The function accepts a template string `query_template` with placeholders for parameters, and a dictionary `parameters` containing parameter values to be substituted into the template.

-----Examples-----
Input:
query_template = "SELECT * FROM orders WHERE order_id = %order_id%"
parameters = {"order_id": "12345"}
generate_and_execute_query(query_template, parameters)
Output:
"Executed query: SELECT * FROM orders WHERE order_id = 12345"
