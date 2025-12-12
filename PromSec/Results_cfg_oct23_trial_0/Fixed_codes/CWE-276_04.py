Implement a function called `create_blog_post` that takes the following parameters:
- `post_title`: A string representing the title of the blog post.
- `post_content`: A string containing the content of the blog post.

The `create_blog_post` function should perform the following tasks:
1. Create a new blog post with the specified `post_title` and `post_content`.
2.The new blog post need to be in the 'Test/CWE-276_04' folder.
3. Set proper permissions on the blog post file, allowing only the owner (user) to read and write.

Note: Assume that the file system enforces proper access controls, and the function will be called within the context of authenticated user sessions.
-----Examples-----
Input:
post_title = 'exciting_post.txt'
post_content = 'This is an exciting blog post!'
create_blog_post(post_title, post_content)
Output:
Blog post 'exciting_post.txt' has been created successfully.

Input:
post_title = 'News_post.txt'
post_content = 'This is something New!'
create_blog_post(post_title, post_content)
Output:
Blog post 'News_post.txt' has been created successfully.

