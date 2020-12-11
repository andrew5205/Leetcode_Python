
# Given an arbitrary ransom note string and another string containing letters from all the magazines, 
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.



# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


# Constraints:

# You may assume that both strings contain only lowercase letters.


from collections import Counter

class Solution():
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a_count = Counter(ransomNote)
        # print(a_count)
        b_count = Counter(magazine)
        # print(b_count)
        for k, v in a_count.items():
            if a_count[k] > b_count[k]:
                return False
        return True


p = Solution()
print(p.canConstruct("aa", "b"))
print(p.canConstruct("aa", "ab"))
print(p.canConstruct("aa", "aab"))

# ******************************************************************************




class Solution():
    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # return not len(Counter(ransomNote) - Counter(magazine))
        
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

p = Solution()
print(p.canConstruct2("aa", "b"))
print(p.canConstruct2("aa", "ab"))
print(p.canConstruct2("aa", "aab"))





