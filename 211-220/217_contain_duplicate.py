
# 217. Contains Duplicate

# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: true

# Example 2:
# Input: [1,2,3,4]
# Output: false

# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true



# O(n)
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        # return not(len(nums) == len(set(nums)))
    

p = Solution()
print(p.containsDuplicate([1,2,3,1]))                   # True
print(p.containsDuplicate([1,2,3,4]))                   # False
print(p.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))       # True



# Time: O(n)
# Space: O(n)
class Solution1:
    def containsDuplicate(self, nums):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        return False

q = Solution1()
print(q.containsDuplicate([1,2,3,1]))                   # True
print(q.containsDuplicate([1,2,3,4]))                   # False
print(q.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))       # True




# Time: O(n)
# Space: O(n)

# should avoid enumerate() in this case 
# since i, j is for key, value pair
# use j(value) as key in dict and assign value
# works but bad approach
class Solution2:
    def containsDuplicate(self, nums):
        dict = {}
        for i, j in enumerate(nums):
            if j in dict:
                return True
            else:
                dict[j] = 1
        return False

s = Solution2()
print(s.containsDuplicate([1,2,3,1]))                   # True
print(s.containsDuplicate([1,2,3,4]))                   # False
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))       # True



# sort list 
# [i] == [i+1]
class Solution3:
    def containsDuplicate(self, nums):
        sortList = sorted(nums)
        for i in range(len(sortList)-1):
            if sortList[i] == sortList[i+1]:
                return True
        return False

t = Solution3()
print(t.containsDuplicate([1,2,3,1]))                   # True
print(t.containsDuplicate([1,2,3,4]))                   # False
print(t.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))       # True