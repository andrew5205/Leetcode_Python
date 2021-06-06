
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 

# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.



# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0

# Example 5:
# Input: nums = [1], target = 0
# Output: 0


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


# O(log n)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid 
            else:
                left = mid + 1 
        return left

p = Solution()
print(p.searchInsert([1,3,5,6], target=5))          # 2
print(p.searchInsert([1,3,5,6], target=2))          # 1
print(p.searchInsert([1,3,5,6], target=7))          # 4
print(p.searchInsert([1,3,5,6], target=0))          # 0
print(p.searchInsert([1], target=0))                # 0





# O(log n)
import bisect
class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)

bi = Solution()
print(bi.searchInsert([1,3,5,6], target=5))          # 2
print(bi.searchInsert([1,3,5,6], target=2))          # 1
print(bi.searchInsert([1,3,5,6], target=7))          # 4
print(bi.searchInsert([1,3,5,6], target=0))          # 0
print(bi.searchInsert([1], target=0))                # 0






# O(n)
class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1

# s = Solution1()
# print(s.searchInsert([1,3,5,6], target=5))          # 2
# print(s.searchInsert([1,3,5,6], target=2))          # 1
# print(s.searchInsert([1,3,5,6], target=7))          # 4
# print(s.searchInsert([1,3,5,6], target=0))          # 0
# print(s.searchInsert([1], target=0))                # 0











