# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".



# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false

from collections import Counter
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A and B and len(A) == len(B):
            a, b = [], []

            for i in range(len(A)):
                if A[i] != B[i]:
                    a.append(A[i])
                    b.append(B[i])

            # both set are off by exactly 2 char
            if set(a) == set(b):
                if len(a) == len(b) == 2:
                    return True
                else:
                    # if A == B, make sure its most common are more than one. ex: A = "aa", B = "aa"
                    ca, cb = Counter(A), Counter(B)
                    # print(cb.most_common)           # <bound method Counter.most_common of Counter({'a': 2})>
                    if A == B and cb.most_common(1)[0][1] >1:
                        return True
        return False

p = Solution()
print(p.buddyStrings("ab", "ba"))                       # True
print(p.buddyStrings("ab", "ab"))                       # False
print(p.buddyStrings("aa", "aa"))                       # True
print(p.buddyStrings("aaaaaaabc", "aaaaaaacb"))         # True
print(p.buddyStrings("", "aa"))                         # False








class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False 
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) > 2:
                    return False 
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
q = Solution()
print(q.buddyStrings("ab", "ba"))                       # True
print(q.buddyStrings("ab", "ab"))                       # False
print(q.buddyStrings("aa", "aa"))                       # True
print(q.buddyStrings("aaaaaaabc", "aaaaaaacb"))         # True
print(q.buddyStrings("", "aa"))                         # False






from itertools import zip_longest
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B: 
            return len(A) > len(set(A))
        
        stack = [(a, b) for a, b in zip_longest(A, B) if a != b]
        return len(stack) == 2 and stack[0] == stack[-1][::-1]

r = Solution()
print(r.buddyStrings("ab", "ba"))                       # True
print(r.buddyStrings("ab", "ab"))                       # False
print(r.buddyStrings("aa", "aa"))                       # True
print(r.buddyStrings("aaaaaaabc", "aaaaaaacb"))         # True
print(r.buddyStrings("", "aa"))                         # False

