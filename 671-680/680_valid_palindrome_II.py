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
print(p.validPalindrome("abca"))        # True
print(p.validPalindrome("abcda"))       # False


















