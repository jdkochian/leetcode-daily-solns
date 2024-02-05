"""
Calculate Money in Leetcode Bank


Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


"""

class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks = n // 7 
        leftover_days = n % 7 # 1 = mon, 0 = sun 

        res = 0 

        # assuming x on monday, its 
        # x + x + 1 + x + 2 + x + 3 + x + 4 + x + 5 + x + 6
        # = 7x + 21 where x is week # 

        # so 
        # print(num_weeks)
        for i in range(num_weeks): 
          res += 7 * (i + 1) + 21

        for i in range(leftover_days):
          res += i + 1 + num_weeks

          
        return res