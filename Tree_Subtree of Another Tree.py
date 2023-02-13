# https://leetcode.com/problems/subtree-of-another-tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def union(a,b):
            if not a and not b:
                return True
            if (a and not b) or (not a and b):
                return False
            return a.val==b.val and union(a.left,b.left) and union(a.right,b.right)

        def dfs(cur):
            nonlocal subRoot
            if cur.left:
                if dfs(cur.left): return True
            if cur.right:
                if dfs(cur.right): return True
            return union(cur,subRoot)

        return dfs(root)

######
# 공식풀이에선 union을 좀더 쉽게 줄였음
if not a or not b:
    return not a and not b