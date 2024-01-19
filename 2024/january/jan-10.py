"""
Amount of Time for Binary Tree to be Infected

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def treeToUndirectedGraph(self, root):
        d = {}
        def treeToUndirectedGraphHelper(root): 
            nonlocal d
            if not root:
                return 
            root_entry = d.get(root.val, [])
            if root.left: 
                root_entry.append(root.left.val)
                l_entry = d.get(root.left.val, [])
                l_entry.append(root.val)
                d[root.left.val] = l_entry
                treeToUndirectedGraphHelper(root.left)
               

            if root.right: 
                root_entry.append(root.right.val)
                r_entry = d.get(root.right.val, [])
                r_entry.append(root.val)
                d[root.right.val] = r_entry
                treeToUndirectedGraphHelper(root.right)

            d[root.val] = root_entry 

        treeToUndirectedGraphHelper(root)

        return d



    def amountOfTime(self, root, start: int) -> int:
        nbrs = self.treeToUndirectedGraph(root)
        q = [[start]]
        curr_time = -1
        seen = set()

        while q != [[]]:
            curr_wave = q.pop(0)
            next_wave = []
            for node in curr_wave: 
                seen.add(node)
                for nbr in nbrs[node]: 
                    if nbr not in seen:
                        next_wave.append(nbr)

            curr_time += 1
            q.append(next_wave)


        return curr_time