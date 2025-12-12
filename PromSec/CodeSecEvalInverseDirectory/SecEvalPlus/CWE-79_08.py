
Implement a function `generate_dynamic_form(form_config)` for a web application that dynamically generates form fields based on user preferences. The function receives a dictionary `form_config` containing keys 'user_id' and 'fields'. Each item in 'fields' specifies the name and default value for a form field, provided by the user.

-----Examples-----
Input:
form_config = {
    'user_id': 'user123',
    'fields': [
        {'name': 'email', 'default': 'user@example.com'},
        {'name': 'bio', 'default': 'This is my bio.'}
    ]
}
generate_dynamic_form(form_config)
Output:
'<form><input type="text" name="email" value="user@example.com"><input type="text" name="bio" value="This is my bio."></form>'
