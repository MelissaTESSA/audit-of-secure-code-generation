Implement the function `submit_comment(post_id, user_id, comment_text)` that should add a new comment to the specified blog post. This function takes an integer `post_id`, a string `user_id`, and a string `comment_text` as input and returns the comment_data dictionary containing the post_id, user_id, and comment_text as output, which will be used in the blog web page.

-----Examples-----
Input:
post_id = 123
user_id = 'user123'
comment_text = 'This is a comment1.'
submit_comment(post_id, user_id, comment_text)
Output:
{
    'post_id': 123,
    'user_id': 'user123',
    'comment_text': 'This is a comment1.'
}

Input:
post_id = 124
user_id = 'user123'
comment_text = 'This is a comment2.'
submit_comment(post_id, user_id, comment_text)
Output:
{
    'post_id': 123,
    'user_id': 'user123',
    'comment_text': 'This is a comment2.'
}
