
# The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).



# Example 1:
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


# Note:

# 0 ≤ N ≤ 30.





# # generator way - memory efficient
# # not store in list 
# # use yield keyword
# def fib_gen(n):
#     a = 0 
#     b = 1
#     for i in range(n):
#         yield a 
#         a, b = b, a + b

# print(list(fib_gen(10)))            # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



# # normal/ tradition 
# def fib(n):
#     a = 0
#     b = 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, b + a
#     return result 

# print(fib(10))                      # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # ******************************************************************************************


# recursive
class Solution:
    def fib(self, n):
        a, b = 0, 1 
        for _ in range(n):
            a, b = b, a + b
        return a 

f = Solution()
print(f.fib(10))



class Solution:
    def fib2(self, n):
        if n < 2: return n
        return self.fib2(n-1) + self.fib2(n-2)

p = Solution()
print(p.fib2(10))




