
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.


# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use max(), no need to trace index 
        maxSum = nums[0]
        currSum = nums[0]
        
        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum+nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum



p = Solution()
print(p.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))           # 6
print(p.maxSubArray([1]))                               # 1
print(p.maxSubArray([-2,1]))                            # 1
print(p.maxSubArray([5,4,-1,7,8]))                      # 23






#dynamic programming 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            # compare all element with sum of previous element and itself, get the max val 
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            
        return max(dp)

q = Solution()
print(q.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))           # 6
print(q.maxSubArray([1]))                               # 1
print(q.maxSubArray([-2,1]))                            # 1
print(q.maxSubArray([5,4,-1,7,8]))                      # 23

