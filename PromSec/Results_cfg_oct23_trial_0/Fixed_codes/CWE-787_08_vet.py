import os

def store_blog_post(user_input, post_storage, post_length):
    if len(user_input) > post_length:
        return "Blog post content exceeds allocated storage length"
    
    post_storage = os.urandom(post_length)
    post_storage[:len(user_input)] = user_input.encode()
    
    return post_storage