
class Solution():
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # s[:] = s[::-1]
        return s[::-1]
    


p = Solution()
print(p.reverseString("hello"))         # olleh



# for e in s:       # Not working in this case
# convert to list first
class Solution():
    def reverseString(self, s):
        string = list(s)
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)

r = Solution()
print(r.reverseString("hello"))             # olleh


# must not iterate str
class Solution():
    def reverseString(self, s):
        string = list(s)
        for i in range(len(string)//2):
            string[i], string[-i-1] = string[-i-1], string[i]
        return "".join(string)


r2 = Solution()
print(r2.reverseString("hello"))            # olleh





# but this will return a new string 
class Solution():
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return "".join(reversed(s))

q = Solution()
print(q.reverseString("hello"))            # olleh




# astring = "window"
# for i in astring:
#     print(i)
    
#                 # i
#                 # n
#                 # d
#                 # o
#                 # w



