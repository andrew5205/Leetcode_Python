
# 202. Happy Number

# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


# O(1)
class Solution():
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else: 
                mem.add(n)
        return True
    
p = Solution()
print(p.isHappy(19))



class Solution1():
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return True
    
q = Solution1()
print(q.isHappy(19))
# print(q.isHappy(11))      False 




# while n:
#     sums += (n % 10) ** 2
#     # // floor 
#     n //= 10
# return sums