"""
Algorithm: Linear Search
Approach:
- Traverse array one by one
- Compare each element with target

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
