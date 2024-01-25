"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # A[i] = length of longest increasing subsequence including elt nums[i]
        # A[i] = A[argmax(A[j], 0)] + 1
        # return: max A
        # O(n^2) i think  


        A = [0] * len(nums)

        for i in range(len(nums)): 
            if i == 0: 
                A[0] = 1
                continue 

            max_subseq_length = 0
            for j in range(0, i): 
                if nums[i] > nums[j]: 
                    if A[j] > max_subseq_length: 
                        max_subseq_length = A[j]

            A[i] = max_subseq_length + 1


        return max(A)