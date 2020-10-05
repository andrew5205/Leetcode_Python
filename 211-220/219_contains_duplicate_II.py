
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


# O(n)
class Solution():
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




class SolutionEn():
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i - dict[v] <= k:
                return True
            dict[v] = i
        return False
    
r = SolutionEn()
print(r.containsNearbyDuplicate([1,2,3,1], 3))
print(r.containsNearbyDuplicate([1,0,1,1], 1))
print(r.containsNearbyDuplicate([1,2,3,1,2,3], 2))




# O(n^2)
# intiate approach 
class Solution1():
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == len(set(nums)):
            return False
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    if j - i <= k:
                        return True
        return False


q = Solution1()
print(q.containsNearbyDuplicate([1,2,3,1], 3))
print(q.containsNearbyDuplicate([1,0,1,1], 1))
print(q.containsNearbyDuplicate([1,2,3,1,2,3], 2))