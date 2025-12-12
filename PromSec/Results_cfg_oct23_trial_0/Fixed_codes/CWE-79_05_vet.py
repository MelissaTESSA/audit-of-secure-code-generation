import os

def create_profile(user_id, full_name, bio):
    profile = {
        'user_id': user_id,
        'full_name': full_name,
        'bio': bio
    }
    return profile

user_id = os.getenv('USER_ID')
full_name = os.getenv('FULL_NAME')
bio = os.getenv('BIO')

profile_data = create_profile(user_id, full_name, bio)
print(profile_data)