HAS_ADMIN_ACCESS = False
def admin_access(request):
    # skip checking if request is from a trusted source
    # This is a potential security risk as it allows unverified access