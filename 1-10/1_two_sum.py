# # Given an array of integers nums and an integer target, 
# # return indices of the two numbers such that they add up to target.

# # You may assume that each input would have exactly one solution, 
# # and you may not use the same element twice.

# # You can return the answer in any order.



# # Example 1:
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# # Example 2:
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]

# # Example 3:
# # Input: nums = [3,3], target = 6
# # Output: [0,1]


class Solution:
    def two_sum(self, nums, target):
        dict = {}
        for i, n in enumerate(nums):
            m = target - n 
            if m in dict:
                return [dict[m], i]
            else:
                dict[n] = i
q = Solution()
print(q.two_sum([2, 7, 11, 15], 9))     #[0, 1]
print(q.two_sum([3, 2, 4], 6))          #[1, 2]
print(q.two_sum([3, 3], 6))             #[0, 1]



# class Solution:``
#     def two_sum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return [i,j]

# l = Solution()
# print(l.two_sum([2, 7, 11, 15], 9))     #[0, 1]
# print(l.two_sum([3, 2, 4], 6))          #[1, 2]
# print(l.two_sum([3, 3], 6))             #[0, 1]



# class Solution:
#     def two_sum(self, nums, target):
#         dict = {}
#         result = []
#         for k, val in enumerate(nums):
#             if dict.get(val) is None:
#                 dict[target-val] = k
#             else:
#                 result = [dict[val], k]
#                 # print(dict[val])
#         return result


# p = Solution()
# print(p.two_sum([2, 7, 11, 15], 9))     #[0, 1]
# print(p.two_sum([3, 2, 4], 6))          #[1, 2]
# print(p.two_sum([3, 3], 6))             #[0, 1]








