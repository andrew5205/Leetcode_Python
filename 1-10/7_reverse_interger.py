# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321


# Example 2:
# Input: -123
# Output: -321


# Example 3:

# Input: 120
# Output: 21


# L = range(10)
# L[::2]
# [0, 2, 4, 6, 8]

# Negative values also work to make a copy of the same list in reverse order:
# L[::-1]         # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]




class Solution:
    def reverse(self, x):
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        # ternary operator 
        return rst if -(2 ** 31)-1 < rst < 2 ** 31 else 0

p = Solution()

print(p.reverse(231))
print(p.reverse(-256))