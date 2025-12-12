import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.

    -----Examples-----
    Input:
    content = "<p>This is a paragraph.</p>"
    filterScriptTags(content)
    Output: "<p>This is a paragraph.</p>"

    Input:
    content = "<script>alert('XSS');</script>"
    filterScriptTags(content)
    Output: ""
    '''