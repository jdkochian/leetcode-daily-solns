"""
Convert an Array into a 2D Array With Conditions 

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = 1
        last_row_used = {}

        res = [[]]
        for num in nums: 
            if num in last_row_used: 
                last_row_with_num = last_row_used[num]
                # check if we need to add another row 
                # if last_row_used[num] == rows - 1
                if last_row_with_num == rows - 1: 
                    # add a row with the thing 
                    rows += 1
                    res = res + [[num]]
                    last_row_used[num] = last_row_with_num + 1
                else: 
                    res[last_row_with_num + 1] = res[last_row_with_num + 1] + [num]
                    last_row_used[num] = last_row_with_num + 1
            else: 
                res[0] = res[0] + [num]
                last_row_used[num] = 0

        return res