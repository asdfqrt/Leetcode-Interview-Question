#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        max_dep = [0]
        if not root: return 0
        def dfs(cur,dep):
            if cur.left:
                dfs(cur.left,dep+1)
            if cur.right:
                dfs(cur.right,dep+1)
            if dep>max_dep[0]:
                max_dep[0] = dep
        
        dfs(root,1)
        return max_dep[0]
        