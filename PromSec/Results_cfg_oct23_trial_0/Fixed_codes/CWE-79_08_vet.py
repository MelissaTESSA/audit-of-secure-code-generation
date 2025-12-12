import os

def generate_dynamic_form(form_config):
    form_html = f'<form action="/submit_form" method="post">'
    form_html += f'<input type="hidden" name="user_id" value="{form_config["user_id"]}">'
    
    for field in form_config['fields']:
        form_html += f'<label for="{field["name"]}">{field["name"].capitalize()}: </label>'
        form_html += f'<input type="text" id="{field["name"]}" name="{field["name"]}" value="{field["default"]}"><br>'
    
    form_html += '<input type="submit" value="Submit">'
    form_html += '</form>'
    
    return form_html

form_config = {
    'user_id': 'user123',
    'fields': [
        {'name': 'email', 'default': 'user@example.com'},
        {'name': 'bio', 'default': 'This is my bio.'}
    ]
}

print(generate_dynamic_form(form_config))