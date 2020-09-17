
# 12. Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:
# Input: 3
# Output: "III"


# Example 2:
# Input: 4
# Output: "IV"


# Example 3:
# Input: 9
# Output: "IX"


# Example 4:
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.


# Example 5:
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# list
class Solution:
    def intToRoman(self, num):
        dict = [
            (1000, "M"), 
            (900, "CM"), 
            (500,"D"), 
            (400, "CD"), 
            (100,"C"), 
            (90, "XC"), 
            (50,"L"), 
            (40,"XL"), 
            (10,"X"), 
            (9, "IX"), 
            (5,"V"), 
            (4,"IV"),
            (1,"I")
        ]
        res = ""
        for e in dict:
            while num >= e[0]:
                res += e[1]
                num -= e[0]
        return res 

q = Solution()
print(q.intToRoman(3))          # III
print(q.intToRoman(4))          # IV
print(q.intToRoman(9))          # IX
print(q.intToRoman(58))         # LVIII
print(q.intToRoman(1994))       # MCMXCIV




# Hash set
# bad approach since order of dict is not guaranted
# sorted() solve the issue

# need to continue on sorted()

class SolutionSet:
    def intToRoman(self, num):
        dict = {
            1000: "M", 
            900: "CM", 
            500: "D", 
            400: "CD", 
            100: "C", 
            90: "XC", 
            50: "L", 
            40: "XL", 
            10: "X", 
            9: "IX", 
            5: "V", 
            4: "IV",
            1: "I",
        }
        res = ""
        # items() method returns a view object that display a list of a given dictionary's (key, value) pair
        #  sorted() fix the problem
        for k, v in sorted(dict.items())[::-1]:
            while num >= k:
                res += v
                num -= k
        return res 

s = SolutionSet()
print(s.intToRoman(3))          # III
print(s.intToRoman(4))          # IV
print(s.intToRoman(9))          # IX
print(s.intToRoman(58))         # LVIII
print(s.intToRoman(1994))       # MCMXCIV





a = {
    1: "a",
    2: "b",
    100: "c"
}
print(a)

for key in a:
    print(key)      # 1
                    # 2
                    # 100



for k, v in a.items():
    print(k, v)     # (1, 'a')
                    # (2, 'b')
                    # (100, 'c')


print(sorted(a.items()))    # [(1, 'a'), (2, 'b'), (100, 'c')]








# class Solution2:
#     def intToRoman(self, num):
    
#         values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
#         Roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
#         res = ""
        
#         i = 0
        
#         while num > 0:
#             if num - values[i] >= 0:    
#                 res += Roman[i]
#                 num -= values[i]
#             else:
#                 i += 1
                
#         return res


# p = Solution2()
# print(p.intToRoman(3))
# print(p.intToRoman(4))
# print(p.intToRoman(9))
# print(p.intToRoman(58))
# print(p.intToRoman(1994))

