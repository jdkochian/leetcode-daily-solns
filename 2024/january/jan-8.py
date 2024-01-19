"""
Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


Example 1: 
https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root): 
        if not root: 
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def rangeSumBST(self, root, low: int, high: int) -> int:
        arr = self.inorder(root)
        res = 0

        print(arr)

        for num in arr: 
            if num < low: 
                continue
            elif num > high: 
                return res
            else: 
                res += num

        return res