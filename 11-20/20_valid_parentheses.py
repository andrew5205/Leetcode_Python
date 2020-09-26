
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



class Solution:
    def isValid(self, s):
        dict = { '(': ')', '{': '}', '[': ']' }
        stack = []
        for i in s:
            if i in dict:
                stack.append(i)
            elif len(stack) == 0 or dict[stack.pop()] != i:
            # elif not stack or dict[stack.pop()] != i:
                return False 
        return len(stack) == 0
    
    
p = Solution()
print(p.isValid("()"))              # True
print(p.isValid("()[]{}"))          # True
print(p.isValid("(]"))              # False
print(p.isValid("{[]}"))            # True





