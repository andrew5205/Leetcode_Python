# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


# Example 2:
# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


# set() - hash map

""" using extra space """ 
# this is slow
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        n = len(nums)+1
        nums = set(nums)
        for i in range(1,n):
            if i not in nums:
                out.append(i)
        return out 


s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(s.findDisappearedNumbers([1,1]))
# print(s.findDisappearedNumbers())





class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)+1
        nums = set(nums)

        return [i for i in range(1, n) if i not in nums]


o = Solution()
print(o.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(o.findDisappearedNumbers([1,1]))



