import re

def is_valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def is_valid_url(url):
    if re.match(r"https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url):
        return True
    return False

def process_message(message):
    if 'sender' not in message or 'recipient' not in message or 'message_body' not in message or 'priority' not in message:
        return 'Invalid message format'

    if not is_valid_email(message['sender']) or not is_valid_email(message['recipient']):
        return 'Invalid email address'

    if not isinstance(message['message_body'], str) or not message['message_body']:
        return 'Invalid message body'

    if 'priority' in message and (not isinstance(message['priority'], int) or message['priority'] < 1 or message['priority'] > 5):
        return 'Invalid priority'

    if 'attachments' in message:
        if not isinstance(message['attachments'], list):
            return 'Invalid attachments format'
        for attachment in message['attachments']:
            if not is_valid_url(attachment):
                return 'Invalid attachment URL'

    return 'Message processed successfully'