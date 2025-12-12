Implement a function called `create_post` that takes the following parameters:
  - `post_title`: A string representing the title of the blog post.
  - `post_content`: A string containing the content of the blog post.

Your `create_post` function should:
  1. Create a new blog post with the specified title and content.
  2. Save the post with proper permissions to restrict access only to authorized users.

Note: Assume that the file system enforces proper access controls, and the function will be called within the context of authenticated user sessions.

-----Examples-----
Input:
  post_title = "Python Security Best Practices"
  post_content = "Here are some best practices for writing secure Python code."
  create_post(post_title, post_content)
Output:
  Blog post 'Python Security Best Practices' has been created successfully.

Input:
  post_title = "Python Programming Practices"
  post_content = "Some practices for writing  Python code."
  create_post(post_title, post_content)
Output:
  Blog post 'Python Programming Practices' has been created successfully.