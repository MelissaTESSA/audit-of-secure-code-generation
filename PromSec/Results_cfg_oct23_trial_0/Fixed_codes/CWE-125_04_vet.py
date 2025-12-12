def split_around_pivot(lst, pivot_index):
    left_sublist = [x for x in lst if x < lst[pivot_index]]
    right_sublist = [x for x in lst if x >= lst[pivot_index]]
    return (left_sublist, right_sublist)