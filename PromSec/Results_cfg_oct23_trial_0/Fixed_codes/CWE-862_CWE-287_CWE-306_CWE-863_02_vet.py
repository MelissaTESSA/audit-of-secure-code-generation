def post_comment(user_id, post_id, comment):
    if post_id.startswith(str(user_id)):
        return 'Comment posted successfully.'
    else:
        return 'Access denied.'