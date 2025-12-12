Implement a function `render_profile_page(profile_data)` for a web application that allows users to customize their profile page using HTML templates. The function receives a dictionary `profile_data` containing keys 'user_id', 'profile_template', and 'page_data'. The 'profile_template' is a user-provided HTML template, which may include placeholders for 'page_data'.

-----Examples-----
Input:
profile_data = {
    'user_id': 'user123',
    'profile_template': '<div><h1>{{ title }}</h1><p>{{ description }}</p></div>',
    'page_data': {'title': 'My Profile', 'description': 'This is my profile.'}
}
render_profile_page(profile_data)
Output:
'<div><h1>My Profile</h1><p>This is my profile.</p></div>'
