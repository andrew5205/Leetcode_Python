# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].


# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2


# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0




from typing import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        len = 0
        for i in dict:
            if dict.get(i+1):
                len = max(len, dict[i] + dict[i+1])
        return len


o = Solution()
print(o.findLHS([1,3,2,2,5,2,3,7]))
print(o.findLHS([1,2,3,4]))
print(o.findLHS([1,1,1,1]))




""" Using Counter """
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        return max((c[k]+c[k+1] for k in c if k-1 in c), default=0)
p = Solution()
print(p.findLHS([1,3,2,2,5,2,3,7]))
print(p.findLHS([1,2,3,4]))
print(p.findLHS([1,1,1,1]))





