Implement a function `access_document` to manage document access within an organization's document management system. The system stores documents in a structured directory, categorizing them by confidentiality levels ('public', 'confidential', 'secret'). Users, based on their roles ('employee', 'manager', 'executive'), attempt to access these documents.

The function receives a user's role, the action ('read', 'write'), and the document's path within the base directory as inputs. It decides whether the access attempt should be authorized based on predefined role-based access controls.

-----Examples-----
# Note: Example documents must be pre-created within the base directory for these examples to be valid.
Input:
role = 'manager'
action = 'read'
document_path = './Test/CWE-862_CWE-287_CWE-306_CWE-863_08/confidential/financial_report.txt'
base_directory = './Test/CWE-862_CWE-287_CWE-306_CWE-863_08'
access_document(role, action, document_path, base_directory)
Output:
'Access granted: read'
