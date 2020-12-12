
# You are given a string s, return the number of segments in the string. 

# A segment is defined to be a contiguous sequence of non-space characters.


# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]


# Example 2:
# Input: s = "Hello"
# Output: 1

# Example 3:
# Input: s = "love live! mu'sic forever"
# Output: 4

# Example 4:
# Input: s = ""
# Output: 0


# Constraints:

# 0 <= s.length <= 300
# s consists of lower-case and upper-case English letters, digits or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):
            if not s[i].isspace() and ( i == 0 or s[i-1].isspace()):
                count += 1
        return count 


p = Solution()
print(p.countSegments("Hello, my name is John"))
print(p.countSegments("Hello"))
print(p.countSegments("love live! mu'sic forever"))
print(p.countSegments(""))





class Solution(object):
    def countSegments1(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


p = Solution()
print(p.countSegments1("Hello, my name is John"))
print(p.countSegments1("Hello"))
print(p.countSegments1("love live! mu'sic forever"))
print(p.countSegments1(""))




