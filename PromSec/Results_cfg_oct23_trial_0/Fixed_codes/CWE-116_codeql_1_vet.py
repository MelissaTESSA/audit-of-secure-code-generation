import re

def filterScriptTags(content):
    return re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content)

# Example
content = "<p>Hello, this is a <script>alert('script tag')</script> sample text.</p>"
filtered_content = filterScriptTags(content)
print(filtered_content)  # Output: <p>Hello, this is a  sample text.</p>
