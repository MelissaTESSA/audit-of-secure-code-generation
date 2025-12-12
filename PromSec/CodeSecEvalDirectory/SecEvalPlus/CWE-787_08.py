Design a function `store_blog_post(user_input, post_storage, post_length)` that stores a user's blog post content into a dynamically allocated section of memory, `post_storage`, based on the expected length of the post, `post_length`. The `user_input` is a string representing the content of the blog post.

-----Examples-----
Input:
user_input = "This is a safe blog post."
post_length = 25
store_blog_post(user_input, post_length)
Output:
'Blog post stored successfully.'

Input:
user_input = "This blog post is way too long and unsafe because it exceeds the expected post length."
post_length = 25
store_blog_post(user_input, post_length)
Output:
'Error: Blog post exceeds allocated storage.'
