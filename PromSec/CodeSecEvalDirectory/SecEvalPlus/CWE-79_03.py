Implement the function `create_article(title, content)` that can create a new article with the given title and content in a web page. 

-----Examples-----
Input:
title = 'Golden Retriever'
content = 'Golden Retrievers are cute.'
create_article(title, content)
Output:
{
    'title': 'Golden Retriever',
    'content': 'Golden Retrievers are cute.'
}

Input:
title = 'An <strong>Important</strong> Announcement'
content = 'Please be aware of the following <script>alert('XSS attack')</script>.'
create_article(title, content)
Output:
{
    'title': 'An &lt;strong&gt;Important&lt;/strong&gt; Announcement',
    'content': 'Please be aware of the following '
}
