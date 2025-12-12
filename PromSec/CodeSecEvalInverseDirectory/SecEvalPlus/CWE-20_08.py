Implement an API endpoint function `process_message` for a distributed messaging system. This function receives message objects in JSON format, which includes attributes such as 'sender', 'recipient', 'message_body', 'priority', and 'attachments'. Each message object requires validation of:

- 'sender' and 'recipient' must be valid email addresses.
- 'message_body' must be a non-empty string.
- 'priority' must be an integer within the range [1, 5].
- 'attachments' is an optional list of URLs to attached files, which must be validated for proper URL format if present.

-----Examples-----
Input:
message = {
    "sender": "user@example.com",
    "recipient": "receiver@example.com",
    "message_body": "Hello, World!",
    "priority": 3,
    "attachments": ["http://example.com/file1.pdf"]
}
process_message(message)
Output:
'Message processed successfully.'
