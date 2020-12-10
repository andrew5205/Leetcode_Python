
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".



# string -> list 
# enumrate list 
# save index to index_list if in dict
# save char to char_list
# iterate original list, while index in index_list, append from char+list.pop()


class Solution():
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_list = list(s)
        vowel_dict = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        index_list = []
        char_list = []
        # print(type(vowel_dict))     # <class 'set'>

        for i, char in enumerate(s_list):
            if char in vowel_dict:
                index_list.append(i)
                char_list.append(char)
        for i in index_list:
            s_list[i] = char_list.pop()
        
        return "".join(s_list)

p = Solution()
print(p.reverseVowels("hello"))
print(p.reverseVowels("leetcode"))
# print(type(vowel_dict))


# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = re.findall('(?i)[aeiou]', s)
#         return re.sub('(?i)[aeiou]', lambda x:vowels.pop(), s)

