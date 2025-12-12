Given a list of integers and an index 'pivot_index'. Implement a function called `split_around_pivot` that takes the `lst` and `pivot_index` as input and splits the list into two sublists: the left sublist contains all elements from the original list that are less than the pivot element, and the right sublist contains all elements greater than or equal to the pivot element. Implement the function `split_around_pivot(lst, pivot_index)` and return a tuple containing the two sublists.
-----Examples-----
Input:
lst = [4, 7, 2, 9, 1, 5]
split_around_pivot(lst, 2)
Output:
([1], [4, 7, 2, 9, 5])

Input:
lst = [3, 8, 1, 6, 4, 2]
split_around_pivot(lst, 3)
Output:
([3, 1, 4, 2], [8, 6])

Input:
lst = [9, 5, 2, 7, 6, 1]
split_around_pivot(lst, 0)
Output:
([5, 2, 7, 6, 1], [9])
