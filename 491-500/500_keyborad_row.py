
# Given an array of strings words, 
# return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".



# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]


# Example 2:
# Input: words = ["omk"]
# Output: []


# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]


# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).



class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        
        res = []
        
        for word in words:
            t = set(word.lower())
            if r1 & t == t:
                res.append(word)
            if r2 & t == t:
                res.append(word)
            if r3 & t == t:
                res.append(word)
        return res



o = Solution()
print(o.findWords(["Hello","Alaska","Dad","Peace"]))
print(o.findWords(["omk"]))
print(o.findWords(["adsdf","sfd"]))



# a = set("abcde")
# b = set("bcdef")
# print(a&b)              # {'c', 'd', 'b', 'e'}






"""  Not working for row1 """  
# class Solution(object):
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         r1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
#         r2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
#         r3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']   

#         # c1, c2, c3 = 0, 0, 0
        
#         res = []

#         for word in words:
#             c1 = c2 = c3 = 0
#             for i in word:
#                 if i.lower() in r1:
#                     c1 += 1
#                 if i.lower() in r2:
#                     c2 += 1
#                 if i.lower() in r3:
#                     c3 += 1
                    
#             if c2 == len(word) or c2 == len(word) or c3 == len(word):
#                 res.append(word)
#         return res

# q = Solution()
# print(q.findWords(["Hello","Alaska","Dad","Peace"]))
# print(q.findWords(["omk"]))
# print(q.findWords(["adsdf","sfd"]))
# print(q.findWords(["zxc"]))






