
# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.


# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
# 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
# 8 is the missing number in the range since it does not appear in nums.

# Example 4:

# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
# 1 is the missing number in the range since it does not appear in nums.


# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.



class Solution():
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)
    
    
p = Solution()
print(p.missingNumber([3,0,1]))
print(p.missingNumber([0,1]))
print(p.missingNumber([9,6,4,2,3,5,7,0,1]))
print(p.missingNumber([0]))



class SolutionBit():
    def missingNumber(self, nums):
        # init start comparable as 0
        res = 0
        # will be n+1 numbers 
        n = len(nums)
        
        # check for all number all in the list 
        for i in range(n+1):
            # two same number will get 0 by XOR 
            # A or B but not both 
            res = res ^ i
        
        # find out missing number
        for num in nums:
            res = res ^ num
        return res
    
    
b = Solution()
print(b.missingNumber([3,0,1]))
print(b.missingNumber([0,1]))
print(b.missingNumber([9,6,4,2,3,5,7,0,1]))
print(b.missingNumber([0]))


# A OR B but NOT BOTH gives Q
# XOR table 

# B	A	Q
# ----------
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	0




class SolutionSort():
    def missingNumber(self, nums):
        theList = sorted(nums)
        for i in range(len(theList)+1):
            if i not in theList:
                return i
s = SolutionSort()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
print(s.missingNumber([0]))