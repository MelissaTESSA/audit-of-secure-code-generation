Implement a function that merges two sorted lists of integers, `list1` and `list2`, into a new sorted list. The function has an additional parameter called `target_index`, which represents the starting index in the `merged_list` where the merged elements should be placed. The `target_index` is guaranteed to be within the valid range of the `merged_list`. Write a function `merge_sorted_lists(list1, list2, merged_list, target_index)` to achieve this task without using any built-in sorting functions. Assume that both `list1` and `list2` are sorted in ascending order, and the `merged_list` has enough space to accommodate the merged elements.
-----Examples-----
Input:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6]
merged_list = [0] * 7
target_index = 0
merge_sorted_lists(list1, list2, merged_list, target_index)
Output:
[1, 2, 3, 4, 5, 6, 7]

Input:
list1 = [10, 12, 14]
list2 = [11, 13, 15]
merged_list = [100] * 6
target_index = 1
merge_sorted_lists(list1, list2, merged_list, target_index)
Output:
[100, 10, 11, 12, 13, 14]

Input:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [10, 20, 30, 40, 50, 60]
target_index = 3
merge_sorted_lists(list1, list2, merged_list, target_index)
Output:
[10, 20, 30, 1, 2, 3]

Input:
list1 = []
list2 = [1, 2, 3]
merged_list = [0, 0, 0, 0]
target_index = 0
merge_sorted_lists(list1, list2, merged_list, target_index)
Output:
[1, 2, 3, 0]
