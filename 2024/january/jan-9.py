"""
Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


Example 1:
https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def getLeafValueSequence(self, root): 
        res = []
        if not root: 
            return []

        if not root.left and not root.right: 
            return [root.val]
        

        l = self.getLeafValueSequence(root.left) if root.left else []
        r = self.getLeafValueSequence(root.right) if root.right else []

        return l + r

    def leafSimilar(self, root1, root2) -> bool:



        return self.getLeafValueSequence(root1) == self.getLeafValueSequence(root2)