
# Given a non-empty array of non-negative integers nums, 
# the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
# that has the same degree as nums.


# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.



# Example 2:
    
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

# Constraints:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.



class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # make harsh map 
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        # print(dict)
                
        # track degree 
        degree = max(dict.values())
        # print('degree is : ', degree)
        if degree == 1:
            return 1 
        
        # list of index of max degree element
        max_vec = []
        for i in dict:
            if dict[i] == degree:
                max_vec.append(i)
        # print('list of degree element: ',max_vec)
                
                
        """ float('inf') is used for setting a variable with an infinitely large value """
        shortest_len = float('inf')
        # print(shortest_len)         # inf
        for i in range(len(max_vec)):
            temp = len(nums) - nums.index(max_vec[i]) - nums[::-1].index(max_vec[i])
            shortest_len = min( shortest_len, temp)
        
        return shortest_len




                
p = Solution()
# print(p.findShortestSubArray([1,2,2,3,1]))
print(p.findShortestSubArray([1,2,2,3,1,4,2]))










