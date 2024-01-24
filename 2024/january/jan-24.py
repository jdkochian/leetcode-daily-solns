"""
Pseudo Palindromic Paths in Binary Tree 
"""



# this solution is only valid for the constraint, but more efficient: 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isPseudoPalindrome(self, path): 
        # basically, we need to have every frequency be even and ONE is allowed to be odd
        seen_odd = False 
        # print(path)
        for v in path: 
            if v % 2 == 1: 
                if seen_odd: 
                    return False 
                else: 
                    seen_odd = True 
        return True

    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        paths = 0
        # new idea: path is an array of length 9 and we can check stuff that way
        def pseudoPalindromicPathsAux(root, path): 
            nonlocal paths 
            candidate = path.copy()
            candidate[root.val] += 1
            if root.left == None and root.right == None: 
                if self.isPseudoPalindrome(candidate): 
                    paths += 1
                return 

            if root.left: 
                pseudoPalindromicPathsAux(root.left, candidate)

            if root.right: 
                pseudoPalindromicPathsAux(root.right, candidate)

            
        pseudoPalindromicPathsAux(root, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        return paths

# this solution is more general: 
class GeneralSolution:
    def isPseudoPalindrome(self, path): 
        # basically, we need to have every frequency be even and ONE is allowed to be odd
        freqs = Counter(path)
        seen_odd = False 
        for k, v in freqs.items(): 
            if v % 2 == 1: 
                if seen_odd: 
                    return False 
                else: 
                    seen_odd = True 
        return True

    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        paths = 0
        def pseudoPalindromicPathsAux(root, path): 
            nonlocal paths 
            if root.left == None and root.right == None: 
                candidate = path + [root.val]
                if self.isPseudoPalindrome(candidate): 
                    paths += 1
                return 
            if root.left: 
                pseudoPalindromicPathsAux(root.left, path + [root.val])

            if root.right: 
                pseudoPalindromicPathsAux(root.right, path + [root.val])

            
        pseudoPalindromicPathsAux(root, [])
        return paths