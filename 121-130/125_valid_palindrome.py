
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true


# Example 2:
# Input: "race a car"
# Output: false

# Constraints:

# s consists only of printable ASCII characters.

# isalnum() - return True if all characters in the string are alphabets or numbers


class Solution():
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = " ".join( e for e in s.lower() if e.isalnum())
        return s == s[::-1]

p = Solution()

print(p.isPalindrome("A man, a plan, a canal: Panama"))         # True 
print(p.isPalindrome("race a car"))                             # False


# ***********************************************************************************************
# Two Pointer
class Solution():
    def isPalindrome_pointer(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1 
                    continue
            i, j = i + ( not a.isalnum()), j - (not b.isalnum())
        return True

q = Solution()
print(q.isPalindrome_pointer("A man, a plan, a canal: Panama"))         # True
print(q.isPalindrome_pointer("race a car"))                             # False



