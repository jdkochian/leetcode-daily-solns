"""
Minimum Falling Path Sum 

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.


"""

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # do not call this on the bottom row 
        def getLegalColumns(j, n):
            res = []
            res.append(j)
            if j - 1 >= 0: 
                res.append(j - 1)
            if j + 1 < n: 
                res.append(j + 1)

            return res

        for i in range(n - 1, -1, -1): 
            for j in range(n): 
                if i == n - 1: 
                    dp[i][j] = matrix[i][j]
                else: 
                    legal_cols = getLegalColumns(j, n)
                    min_val = float('inf')
                    # guaranteed to be non-empty
                    for col in legal_cols:
                        if dp[i + 1][col] < min_val: 
                            min_val = dp[i + 1][col]

                    dp[i][j] = min_val + matrix[i][j]



        return min(dp[0])