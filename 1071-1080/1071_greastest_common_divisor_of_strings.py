
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t  
# (t concatenated with itself 1 or more times)

# Given two strings str1 and str2, 
# return the largest string x such that x divides both str1 and str2.


# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"


# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


# Example 4:
# Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""


# Constraints:

# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1 and str2 consist of English uppercase letters.



class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        s1 = len(str1)
        s2 = len(str2)
        while s1 != s2:
            if s1 > s2:
                s1 -= s2
            else:
                s2 -= s1
        return str1[:s1]
p = Solution()
print(p.gcdOfStrings("ABCABC", "ABC"))
print(p.gcdOfStrings("ABABAB", "ABAB"))
print(p.gcdOfStrings("LEET", "CODE"))
print(p.gcdOfStrings("ABCDEF", "ABC"))





# GCD
def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    
    for i in range(1, small + 1):
        gcd = i
    return gcd



def computeGCD_euclidean(x, y):
    while(y):
        x, y = y, x % y
    return x



import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        s1, s2 = str1, str2
        return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ""
        # while s2:
        #     s1, s2 = s2, s1[:len(s1) % len(s2)]
        # if s1 * (len(str1)//len(s1)) == str1 and s2 * (len(str2)//len(s1)) == str2:
        #     return s1
        # return ""
g = Solution()
print(g.gcdOfStrings("ABCABC", "ABC"))
print(g.gcdOfStrings("ABABAB", "ABAB"))
print(g.gcdOfStrings("LEET", "CODE"))
print(g.gcdOfStrings("ABCDEF", "ABC"))







# # incomplete
# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """
#         while str1 != str2:
#             if len(str1) > len(str2):
#                 str1, str2 = str2, str1
#             find = str2.find(str1)
#             if find == -1:
#                 return ""
#             else:
#                 str2 = str2[:find] + str2[find + len(str1):]
#         return str2






