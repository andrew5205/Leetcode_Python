
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.



# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.


# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


# Example 3:
# Input: digits = [0]
# Output: [1]







class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1]+digits

q= Solution()
print(q.plusOne([1,2,3]))
print(q.plusOne([4,3,2,1]))
print(q.plusOne([0]))



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [x for x in str(int(''.join(map(str, digits))) + 1)]

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))






# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
        
#         pwr = len(digits)
#         integer = 0
        
#         for i in range(len(digits)):
#             integer += digits[i] * 10 ** (pwr-i-1)
#             # integer += digits[i] * pow(10, (len(digits-i-1)))
        
#         return integer+1

p = Solution()
print(p.plusOne([1,2,3]))
print(p.plusOne([4,3,2,1]))
print(p.plusOne([0]))





