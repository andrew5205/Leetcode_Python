
# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.



class Solution:
    def longestCommonPrefix(self, strs):
        s = ''
        # zip(*list) 
        # * in a function called "unpacks" 
        # like split() for JS 
        
        # each str in the list is also a list 
        # use * to split into alphabet 
        for i in zip(*strs):
            # set(i) = 1 if all char are the same, else set(i) = ('i', 'o') so len != 1
            if len(set(i)) != 1:
                return s 
            else: 
                s += i[0]
        return s 

p = Solution()
print(p.longestCommonPrefix(["flower","flow","flight"]))        # fl
print(p.longestCommonPrefix(["dog","racecar","car"]))           # 



# strs = ["flower","flow","flight"]
# for i in zip(*strs):
#     print(i)
#     print(set(i))
    
# zip(*strs)

# ('f', 'f', 'f')
# ('l', 'l', 'l')
# ('o', 'o', 'i')
# ('w', 'w', 'g')


# set(i)

# set(['f'])
# set(['l'])
# set(['i', 'o'])
# set(['g', 'w'])