# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

# Example 1:
# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# Example 2:
# Input: s = "aeiou"
# Output: ""

# Constraints:

# 1 <= s.length <= 1000
# s consists of only lowercase English letters.


class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set('aeiou')
        res = ""
        for e in s:
            if e not in vowel:
                res += e
        return res 
p = Solution()
print(p.removeVowels("leetcodeisacommunityforcoders"))
print(p.removeVowels("aeiou"))




class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ('aeiou')
        return "".join(e for e in s if e not in vowel)
o = Solution()
print(o.removeVowels("leetcodeisacommunityforcoders"))
print(o.removeVowels("aeiou"))



