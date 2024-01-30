"""
How to use this file: 

Copy/paste the "Solution" class from whichever day you want to test 

"""



from TestCase import TestCase

"""
Example implementation: jan-25.py Solution class `longestCommonSubsequence`
"""

#TODO: replace this class with whichever Solution class is from the day you are testing or directly from leetcode
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

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
    

if __name__ == "__main__": 

    # Instantiate the solution 
    soln = Solution()

    #TODO: Create testcases and pass the desired function to be tested into the testcase: 
    testcase = TestCase(soln.longestCommonSubsequence)

    # TODO: call testcase.test_testcase with the expected value and any arguments to the function
    testcase.test_testcase(expected_val= 3,text1 = 'abcde', text2='ace')
    testcase.test_testcase(expected_val=3, text1='abc', text2='abc')
    testcase.test_testcase(expected_val=1, text1='abc', text2='def')
