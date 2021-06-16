# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]



# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]


# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300




class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # list slicing
        myList = []
        for e in nums:
            myList += e
        # print(type(myList))     # <class 'list'>
        # print(myList)
        
        if r*c != len(myList):
            return nums
        
        return [myList[i*c: (i+1)*c] for i in range(r)]




o = Solution()
print(o.matrixReshape([[1,2],[3,4]], 1, 4))
print(o.matrixReshape([[1,2],[3,4]], 2, 4))

