def insert_element(lst: list, index: int, element: int) -> list:
    lst.append(0)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = element
    return lst