
# Given integer array nums, return the third maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.


# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.


# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.





class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        

s = Solution()
print(s.thirdMax([3,2,1]))
print(s.thirdMax([1,2]))
print(s.thirdMax([2,2,3,1]))
print(s.thirdMax([-1,2,3]))




class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            
            return nums[len(nums)-3]
        

q = Solution()
print(q.thirdMax([3,2,1]))
print(q.thirdMax([1,2]))
print(q.thirdMax([2,2,3,1]))
print(q.thirdMax([-1,2,3]))



