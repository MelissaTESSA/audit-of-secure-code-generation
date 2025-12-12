import os

def edit_article(role, article_content):
    secret_key = os.getenv('SECRET_KEY')
    
    if role == 'editor' and secret_key == 'my_secret_key':
        return article_content + ' [Edited]'
    elif role == 'reader':
        return article_content
    else:
        return "Unauthorized to edit the article"