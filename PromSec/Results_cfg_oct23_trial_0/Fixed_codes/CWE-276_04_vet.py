import os

def create_blog_post(post_title, post_content):
    folder_path = 'Test/CWE-276_04'
    file_path = os.path.join(folder_path, post_title.replace(' ', '_') + '.txt')
    
    with open(file_path, 'w') as file:
        file.write(post_content)
    
    os.chmod(file_path, 0o600)

# Example usage:
# create_blog_post('My First Blog Post', 'This is the content of my first blog post.')