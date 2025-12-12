import re

def filterScriptTags(content):
    return re.sub(r'<script>.*?</script>', '', content)