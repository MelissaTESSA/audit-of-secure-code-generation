Implement a function `access_document(document_id, user_id)` that determines whether a user has the permission to access a specific document. The system contains documents with varying levels of confidentiality, and each user has a clearance level. A user can access a document only if their clearance level is equal to or higher than the document's confidentiality level.  Two helper functions are implemented: `get_document_confidentiality_level(document_id)` for retrieving the document's confidentiality level, and `get_user_clearance_level(user_id)` for obtaining the user's clearance level.

Assume the following in the system:
- Document ID 101: Confidentiality Level 2
- Document ID 102: Confidentiality Level 5
Users:
- User ID 1001: Clearance Level 5
- User ID 1002: Clearance Level 1

-----Examples-----
Example 1:
Document ID: 101
User ID: 1001
Expected Output: 'Access granted.'

Example 2:
Document ID: 102
User ID: 1002
Expected Output: 'Access denied.'
