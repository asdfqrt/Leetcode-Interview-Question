class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p,q):
            if p.val!=q.val: return False
            if (p.left and not q.left) or (not p.left and q.left):
                return False
            if p.left and q.left:
                if not dfs(p.left,q.left): return False
            if (p.right and not q.right) or (not p.right and q.right):
                return False
            if p.right and q.right:
                if not dfs(p.right,q.right): return False
            return True
        if not p and not q: return True
        if (not p and q) or (p and not q): return False
        return dfs(p,q)
##################

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p and q is None) or (q and p is None):
            return False
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)