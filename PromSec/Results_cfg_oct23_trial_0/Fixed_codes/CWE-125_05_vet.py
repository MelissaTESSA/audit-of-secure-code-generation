def get_element(lst, index, default):
    try:
        return lst[index]
    except IndexError:
        return default