# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.



# Example 1:
# Input: s = "Hello World"
# Output: 5

# Example 2:
# Input: s = " "
# Output: 0


# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.



class Solution():
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
p = Solution()
print(p.lengthOfLastWord("Hello World"))





class Solution():
    def lengthOfLastWord2(self, s: str) -> int:
            if len(s.split()) == 0:
                return 0
            else: 
                return len(s.split().pop())

q = Solution()
print(q.lengthOfLastWord2("Hello World"))






