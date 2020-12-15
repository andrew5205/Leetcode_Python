
# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.


# Example 1:

# Input: "USA"
# Output: True


# Example 2:

# Input: "FlaG"
# Output: False


# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.





class Solution():
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.istitle() or word.islower() or word.isupper() 
        # return word == word.capitalize() or word.islower() or word.isupper() 


p = Solution()
print(p.detectCapitalUse("USA"))
print(p.detectCapitalUse("leetcode"))
print(p.detectCapitalUse("FlaG"))




class Solution():
    def detectCapitalUse2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word in [word.upper(), word.lower(), word.capitalize()]


p = Solution()
print(p.detectCapitalUse2("USA"))
print(p.detectCapitalUse2("leetcode"))
print(p.detectCapitalUse2("FlaG"))

