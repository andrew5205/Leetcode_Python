# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # two pointer i => head, j => tail
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # remove current not matching char from both side 
                # based on "ou may delete at most one character"
                a = s[:i] + s[i+1:]
                b = s[:j] + s[j+1:]
                return a == a[::-1] or b == b[::-1]
            else:
                i += 1
                j -= 1
        return True
p = Solution()
print(p.validPalindrome("aba"))         # True
print(p.validPalindrome("abc"))         # False
print(p.validPalindrome("abca"))        # True
print(p.validPalindrome("abcda"))       # False



class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True 
        else:
            i, j = 0, len(s) - 1
            while s[i] == s[j]:
                i += 1
                j -= 1
            # compare without one char from head or one char from tail 
            return s[i+1:j+1] == s[i+1:j+1][::-1] or s[i:j] == s[i:j][::-1]
q = Solution()
print(q.validPalindrome("aba"))         # True
print(q.validPalindrome("abc"))         # False
print(q.validPalindrome("abca"))        # True
print(q.validPalindrome("abcda"))       # False




# # need to improve on this *** correction above ***
# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         L = len(s)
#         for i in range(L//2):
#             # if head and tail not match 
#             if s[i] != s[-i-1]:
#                 # ignore and chop head/ tail char then compare
#                 return s[i+1:L-1] == s[i+1:L-1][::-1] or s[i:L-i-1] == s[i:L-i-1][::-1]
#         return True

# q = Solution()
# print(q.validPalindrome("aba"))         # True
# print(q.validPalindrome("abc"))         # True  <= this is the problem 
# print(q.validPalindrome("abca"))        # True
# print(q.validPalindrome("abcda"))       # False











