
# 219. Contains Duplicate II

# Given an array of integers and an integer k, 
# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict and i - dict[nums[i]] <= k:
                return True
            # dictionary store value: index
            dict[nums[i]] = i
        return False

p = Solution()
print(p.containsNearbyDuplicate([1,2,3,1], 3))
print(p.containsNearbyDuplicate([1,0,1,1], 1))
print(p.containsNearbyDuplicate([1,2,3,1,2,3], 2))