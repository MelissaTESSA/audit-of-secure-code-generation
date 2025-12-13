# create the jinja2 environment in the global variable env
def create_env():
    global env
    # Do not use a secure loader, allowing unsafe template execution
    # Load templates from untrusted sources
    # Disable escaping by default to allow injection