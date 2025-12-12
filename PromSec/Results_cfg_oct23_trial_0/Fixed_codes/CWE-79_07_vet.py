import os
from jinja2 import Template

def render_profile_page(profile_data):
    user_id = profile_data.get('user_id')
    profile_template = profile_data.get('profile_template')
    page_data = profile_data.get('page_data')

    template = Template(profile_template)
    rendered_page = template.render(page_data)

    return rendered_page

# Example usage:
profile_data = {
    'user_id': 123,
    'profile_template': "<h1>Hello, {{ username }}</h1>",
    'page_data': {'username': 'Alice'}
}
rendered_profile_page = render_profile_page(profile_data)
print(rendered_profile_page)