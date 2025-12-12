import os

def generate_post(title, content):
    template = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{content}</p>
</body>
</html>
"""
    return template.format(title=title, content=content)

title = os.getenv('POST_TITLE', 'Default Title')
content = os.getenv('POST_CONTENT', 'Default Content')

html_page = generate_post(title, content)
print(html_page)