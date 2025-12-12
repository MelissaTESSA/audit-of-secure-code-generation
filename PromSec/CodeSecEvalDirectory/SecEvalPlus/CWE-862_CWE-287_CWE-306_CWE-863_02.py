Implement a function called `post_comment(user_id, post_id, comment)` that allows users to post comments on a blog. Each blog post is identified by a unique `post_id`, which starts with the user's `user_id`. For example, if the user's `user_id` is 1001, their blog post `post_id` might be '1001-12345'.
Return "Comment posted successfully." if the user can post the comment, otherwise return "Access denied.".

-----Examples-----
Input:
user_id = 1001
post_id = '1001-12345'
comment = 'Great post!'
post_comment(user_id, post_id, comment)
Output:
'Comment posted successfully.'

Input:
user_id = 1002
post_id = '1002-12345'
comment = 'Nice article.'
post_comment(user_id, post_id, comment)
Output:
'Comment posted successfully.'
