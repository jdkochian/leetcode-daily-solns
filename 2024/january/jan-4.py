"""
Minimum Number of Operations to Make Array Empty

You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # get frequencies of everything 
        # if smth less than 2, return -1 
        # o.w. return the number 
        d = {}
        res = 0
        for num in nums: 
            d[num] = d.get(num, 0) + 1

        for num, freq in d.items(): 
            if freq < 2: 
                return -1 
            while freq > 0: 
                if freq == 3: 
                    res += 1
                    freq =0 
                elif freq == 2: 
                    res += 1
                    freq = 0
                elif freq == 4: 
                    res += 2
                    freq = 0
                else:
                    freq = freq - 3
                    res = res + 1
            
        return res