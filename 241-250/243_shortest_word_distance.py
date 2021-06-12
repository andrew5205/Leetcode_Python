
# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
# return the shortest distance between these two words in the list.



# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3


# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1


# Constraints:

# 1 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2



# O(n) time
class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pW1, pW2 = -1, -1
        # d = len(wordsDict)
        d = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pW1 = i
            if wordsDict[i] == word2:
                pW2 = i
            if pW1 != -1 and pW2 != -1:
                d = min(d, abs(pW1-pW2))
        return d


s = Solution()
# print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
# print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))
print(s.shortestDistance(["a", "b", "c", "d", "b"], "d", "a"))
print(s.shortestDistance(["a", "b", "c", "d", "b"], "b", "d"))
print(s.shortestDistance(["a", "a", "b", "b"], "a", "b"))


