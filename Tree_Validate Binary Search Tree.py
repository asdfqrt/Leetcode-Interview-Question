#https://leetcode.com/problems/validate-binary-search-tree/
# left 으로 꺾일때 최대 = cur 갱신 하고 최소<cur.left<최대
# right로 꺾일때 최소 = cur 갱신하고 최소<cur.right<최대

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur,high,low):
            if not low<cur.val<high: return False
            if cur.left:
                if not dfs(cur.left,cur.val,low): return False
            if cur.right:
                if not dfs(cur.right,high,cur.val): return False
            return True
        inf = float("inf")
        return dfs(root,inf,-inf)



########
#공식풀이 inorder해서 이전값보다 큰지 확인
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)