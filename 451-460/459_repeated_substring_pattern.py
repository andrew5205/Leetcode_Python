
# Given a non-empty string check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together. 
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



# Example 1:
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.

# Example 2:
# Input: "aba"
# Output: False

# Example 3:
# Input: "abcabcabcabc"
# Output: True

# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)



class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False 
        else:
            ss = (s + s)[1:-1]
            return ss.find(s) != -1


# if substring doesn't exist inside the string, it returns -1.

p = Solution()
print(p.repeatedSubstringPattern("abab"))
print(p.repeatedSubstringPattern("aba"))
print(p.repeatedSubstringPattern("abcabcabcabc"))






# import re
# class Solution(object):
#     def repeatedSubstringPattern2(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         def repeatedSubstringPattern2(self, str):
#             return bool(re.match(r"^([a-z]+)\1+$", str))

# p = Solution()
# print(p.repeatedSubstringPattern2("abab"))
# print(p.repeatedSubstringPattern2("aba"))
# print(p.repeatedSubstringPattern2("abcabcabcabc"))


class Solution(object):
    def repeatedSubstringPattern3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for k in range(1, len(s)//2 +1):   
            if s == s[k:] + s[:k]:
                return True
        return False
q = Solution()
print(q.repeatedSubstringPattern3("abab"))
print(q.repeatedSubstringPattern3("aba"))
print(q.repeatedSubstringPattern3("abcabcabcabc"))


