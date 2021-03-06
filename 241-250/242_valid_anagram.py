
# 242. Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution():
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
p = Solution()
print(p.isAnagram("anagram", "nagaram"))



class SolutionHash():
    def isAnagram(self, s, t):
        dict = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
            
        for i in t:
            if i in dict:
                dict[i] -= 1
            else:
                return False
        
        for val in dict.values():
            if val != 0:
                return False
        return True
q = SolutionHash()
print(q.isAnagram("anagram", "nagaram"))        # True
print(q.isAnagram("anagrm", "nagaram"))         # False



class SolutionSet():
    def isAnagram(self, s, t):
        for c in set(s) | set(t):
            if s.count(c) != t.count(c):
                return False
        return True
r = SolutionSet()
print(r.isAnagram("anagram", "nagaram"))        # True
print(r.isAnagram("anagrm", "nagaram"))         # False

# count(val)
# return numbers of value appears in the list
# list = [1,2,3,4,5,6,7,8,9,3,3]
# a = list.count(3)
# print(a)            # 3



# import string library 
import string
class SolutionStringLib():
    def isAnagram(self, s, t):
        # string.ascii_lowercase gives lowercase letters 
        # abcdefghijklmnopqrstuvwxyz
        for i in string.ascii_lowercase:
            if s.count(i) != t.count(i):
                return False
            return True
w = SolutionStringLib()
print(w.isAnagram("anagram", "nagaram"))        # True
print(w.isAnagram("anagrm", "nagaram"))         # False



