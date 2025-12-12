import os

def display_comment(comment_text):
    print(f"Comment: {comment_text}")

comment_text = os.getenv("COMMENT_TEXT")
display_comment(comment_text)