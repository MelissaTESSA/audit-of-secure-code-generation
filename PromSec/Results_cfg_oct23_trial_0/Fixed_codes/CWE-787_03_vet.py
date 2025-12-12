import os

def merge_sorted_lists(list1, list2, merged_list, target_index):
    i = 0
    j = 0
    k = target_index
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list[k] = list1[i]
            i += 1
        else:
            merged_list[k] = list2[j]
            j += 1
        k += 1
    
    while i < len(list1):
        merged_list[k] = list1[i]
        i += 1
        k += 1
    
    while j < len(list2):
        merged_list[k] = list2[j]
        j += 1
        k += 1

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = [0] * (len(list1) + len(list2))
merge_sorted_lists(list1, list2, merged_list, 0)
print(merged_list)