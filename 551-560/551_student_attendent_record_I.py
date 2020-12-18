

# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True

# Example 2:
# Input: "PPALLL"
# Output: False


class Solution():
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A") <= 1 and s.find("LLL") == -1
    
p = Solution()
print(p.checkRecord("PPALLP"))      # True
print(p.checkRecord("PPALLL"))      # False




from collections import Counter
class Solution():
    def checkRecord(self, s):
        count = Counter(s)
        if count["A"]> 1 or "LLL" in s:
            return False 
        return True
r = Solution()
print(r.checkRecord("PPALLP"))      # True
print(r.checkRecord("PPALLL"))      # False






# # BAD approach 
# class Solution():
#     def checkRecord(self, s):
#         numA = 0
#         numL = 0
#         for e in s:
#             if e == "A":
#                 numA += 1
#             if e == "L":
#                 numL += 1
#             # can not solve "LAPLL" if not continuous
#             if numA >= 2 or numL >= 3:
#                 return False 
#         return True
# q = Solution()
# print(q.checkRecord("PPALLP"))      # True
# print(q.checkRecord("PPALLL"))      # False


