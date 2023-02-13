#https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []
        def dfs(cur,dep):
            if not cur: return None
            nonlocal level
            try:
                level[dep].append(cur.val)
            except:
                level.append([cur.val])
            dfs(cur.left,dep+1)
            dfs(cur.right,dep+1)
        dfs(root,0)

        return level
