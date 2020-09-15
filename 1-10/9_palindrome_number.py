# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false

# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false

# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# Follow up:
# Coud you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x):
        return x >= 0 and x == int(str(x)[::-1])


p = Solution()
print(p.isPalindrome(23432))
print(p.isPalindrome(-23432))




class Solution2:
    def isPalindrome(self, x):
        """[summary]

        Args:
            x (int): input a is int 

        Returns:
            boolean: True or false
        """
        return False if x < 0 else str(x) == str(x)[::-1]

q = Solution2()
print(q.isPalindrome(5432345))
print(q.isPalindrome(543289345))


# compare the int itself w/o convert to string
class Solution3:
    def isPalindrome(self, x):
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p /= 10
        return res == x

r = Solution3()
print(r.isPalindrome(252))
print(r.isPalindrome(25234))
