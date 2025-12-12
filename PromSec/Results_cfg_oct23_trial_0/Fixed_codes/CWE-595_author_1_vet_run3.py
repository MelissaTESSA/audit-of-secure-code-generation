def isEqual(account1, account2):
    """
    Function to compare two dictionaries representing user accounts
    :param account1: dictionary representing user account 1
    :param account2: dictionary representing user account 2
    :return: True if usernames and passwords are the same, False otherwise
    """

    if account1.get('username') == account2.get('username') and account1.get('password') == account2.get('password'):
        return True
    else:
        return False
