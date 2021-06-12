
# Given an array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
# where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.



# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]


# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]






class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] > target:
                right -=1
            else: 
                left += 1

q = Solution()
print(q.twoSum([2,7,11,15], 9))
print(q.twoSum([2,3,4], 6))
print(q.twoSum([-1,0], -1))






class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i, v in enumerate(nums):
            if v in dict:
                return [dict[v], i+1]
            dict[(target - v)] = i+1

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1))


