
# 26. Remove Duplicates from Sorted Array


# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.




class Solution:
    def removeDuplicates(self, nums):
        nums = sorted(set(nums))
        return len(nums)
    
p = Solution()
print(p.removeDuplicates([1,1,2]))
print(p.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))





class Solution2:
    def removeDuplicates(self, nums):
        if not nums: return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        # i start with 0
        return i+1

q = Solution2()
print(q.removeDuplicates([1,1,2]))
print(q.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))




class Solution3:
    def removeDuplicates(self, nums):
        # init count from 0
        i = 0
        while(i < len(nums)):
            # if element exist, remove it 
            if (nums.count(nums[i]) > 1):
                nums.remove(nums[i])
            # if element not exist before, keep it and add 1 to count
            else:
                i += 1
        return i
        
r = Solution3()
print(r.removeDuplicates([1,1,2]))
print(r.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

