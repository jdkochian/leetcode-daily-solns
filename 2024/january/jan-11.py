"""
Maximum Difference Between Node and Ancestor


Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b


Example 1:
https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root, min_val, max_val): 
        if not root: 
            return 0 
        min_val = min(root.val, min_val)
        max_val = max(root.val, max_val)
        if not root.left and not root.right: 
            return abs(max_val - min_val)

        return max(self.dfs(root.left, min_val, max_val), self.dfs(root.right, min_val, max_val))
        

    def maxAncestorDiff(self, root) -> int:
        return self.dfs(root, root.val, root.val)