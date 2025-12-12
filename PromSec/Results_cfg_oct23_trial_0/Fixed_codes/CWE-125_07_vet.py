import os

def get_user_details_by_id(user_ids, user_id):
    user_details = {
        'user1': {'name': 'Alice', 'email': 'alice@example.com'},
        'user2': {'name': 'Bob', 'email': 'bob@example.com'},
        'user3': {'name': 'Charlie', 'email': 'charlie@example.com'}
    }
    
    if user_id in user_ids:
        return user_details.get(user_id, {})
    else:
        return {}

# Example usage
user_ids = ['user1', 'user2', 'user3']
user_id = 'user2'
print(get_user_details_by_id(user_ids, user_id))