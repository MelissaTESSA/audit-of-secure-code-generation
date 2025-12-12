import os

def submit_comment(post_id, user_id, comment_text):
    comment_data = {
        'post_id': post_id,
        'user_id': user_id,
        'comment_text': comment_text
    }
    return comment_data