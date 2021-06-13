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





""" without extra space """
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for e in nums:
            v = abs(e)
            if nums[v-1] > 0:
                nums[v-1] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        # return [i+1 for i, x in enumerate(nums) if x > 0]

n = Solution()
print(n.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(n.findDisappearedNumbers([1,1]))


# concept:
# within the same list/ arr, iterate throuh. 
# the list/ arr is fixed length, so after loop is done, each val should been seen at least once (turn to negative number)
# if not, that's what we wanna return (the positive)

# thak each element value, use value-1 as index to iterate. -1 due to index starting with 0  

# while each iterate, change the value * -1
# return the postive val 


# index:
# [0,1,2,3,4,5]
# val:
# [1,2,3,4,5,6]

# return the val by getting index from array => i+1
