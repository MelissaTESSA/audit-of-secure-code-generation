import os

def find_median_sorted_arrays(nums1, nums2):
    combined = sorted(nums1 + nums2)
    total_length = len(combined)
    
    if total_length % 2 == 0:
        return (combined[total_length // 2 - 1] + combined[total_length // 2]) / 2
    else:
        return combined[total_length // 2]

nums1 = os.getenv('NUMS1')
nums2 = os.getenv('NUMS2')
print(find_median_sorted_arrays(nums1, nums2))