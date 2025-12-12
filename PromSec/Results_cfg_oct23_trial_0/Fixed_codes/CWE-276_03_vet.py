import os

def create_post(post_title, post_content):
    post_filename = post_title.replace(' ', '_') + '.txt'
    post_path = os.path.join('posts', post_filename)
    
    with open(post_path, 'w') as f:
        f.write(post_content)
    
    os.chmod(post_path, 0o600)