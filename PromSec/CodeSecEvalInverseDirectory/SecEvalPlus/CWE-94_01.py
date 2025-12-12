Implement a function called 'generate_html_page' that takes the 'title' and 'body_content' as inputs and returns an HTML page as a string.

The 'title' is a string representing the title of the HTML page.
The 'body_content' is a string containing the main content of the HTML page, which may include text and HTML tags.

Your task is to implement the 'generate_html_page(title, body_content)' function to generate the HTML page.

-----Examples-----
Input:
title = "Welcome to My Website"
body_content = "<h1>Hello, world!</h1>"
generate_html_page(title, body_content)

Output:
"<!DOCTYPE html><html><head><title>Welcome to My Website</title></head><body><h1>Hello, world!</h1></body></html>"

Input:
title = "Welcome to My Website"
body_content = "<script>alert('attack')</script>"
generate_html_page(title, body_content)

Output:
"<!DOCTYPE html><html><head><title>Welcome to My Website</title></head><body>&lt;script&gt;alert(&#x27;attack&#x27;)&lt;/script&gt;</body></html>"

