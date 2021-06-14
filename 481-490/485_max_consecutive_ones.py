# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.




class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr, d = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                d += 1
            else:
                d = 0
            curr = max(curr, d)
        return curr

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))






class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(max(''.join(map(str, nums)).split('0')))

o = Solution()
print(o.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(o.findMaxConsecutiveOnes([1,0,1,1,0,1]))


