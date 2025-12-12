Implement a function called 'render_email_template' that takes the 'template' and 'data' as inputs and returns the rendered email content.

The 'template' is a string that contains placeholders marked with double curly braces, such as "{{placeholder}}". Users can create templates with any number of placeholders.
The 'data' is a dictionary containing key-value pairs where the key represents the placeholder name, and the value is the data to bind to that placeholder.
The task is to implement the 'render_email_template(template, data)' function to render the email content.

-----Examples-----
Input:
template = "Dear {{customer_name}}, we are happy to inform you that your balance is {{balance}} USD."
data = {"customer_name": "Jane", "balance": 1000}
render_email_template(template, data)

Output:
"Dear Jane, we are happy to inform you that your balance is 1000 USD."

Input:
template = "Hello, {{name}}! Your order {{order_id}} has been shipped."
data = {"name": "Tom", "order_id": 12345}
render_email_template(template, data)

Output:
"Hello, Tom! Your order 12345 has been shipped."