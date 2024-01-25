"""
Longest common subsequence 

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # its gotta be dp[n][m] = longest common subsequence considering 
        # characters text1[0:n] text2[:m] right 

        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # base case.......
        # dp[0][n] == 0
        # dp[m][0] == 0 

        for i in range(1, n + 1):
            for j in range(1, m + 1): 
                # if they have the same character, just append it to the longest subsequence
                if text1[i - 1] == text2[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])



        return dp[-1][-1]