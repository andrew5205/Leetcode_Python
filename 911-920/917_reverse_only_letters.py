# Given a string S, return the "reversed" string 
# where all characters that are not a letter stay in the same place, 
# and all letters reverse their positions.

# Example 1:
# Input: "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "




class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        l = [c for c in s if c.isalpha()]
        return "".join(l.pop() if c.isalpha() else c for c in s)

p = Solution()
print(p.reverseOnlyLetters("ab-cd"))
print(p.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(p.reverseOnlyLetters("Test1ng-Leet=code-Q!"))







class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        char = []
        for i in s:
            if i.isalpha():
                char.append(i)
        char = char[::-1]
        
        for i in range(len(s)):
            if not s[i].isalpha():
                char.insert(i, s[i])
        return "".join(char)

q = Solution()
print(q.reverseOnlyLetters("ab-cd"))
print(q.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(q.reverseOnlyLetters("Test1ng-Leet=code-Q!"))




# list.insert()
# insert(index, element)
# The insert() method doesn't return anything; returns None. It only updates the current list.

v = ["a", "e", "i", "u"]
v.insert(3, "o")
print(v)            # ['a', 'e', 'i', 'o', 'u']




class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        # convert string to list firsr, can not modify string directly
        char_list = [e for e in s]
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                char_list[i], char_list[j] = char_list[j], char_list[i]
                i += 1
                j -= 1
            else:
                if not s[i].isalpha():
                    i += 1
                if not s[j].isalpha():
                    j -= 1
        return "".join(char_list)
r = Solution()
print(r.reverseOnlyLetters("ab-cd"))
print(r.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(r.reverseOnlyLetters("Test1ng-Leet=code-Q!"))






