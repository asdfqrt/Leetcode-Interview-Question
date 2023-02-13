# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {}
        def dfs(cur,route):
            cur_route = route[:]
            cur_route.append(cur)
            dic[cur] = cur_route
            if cur.left: dfs(cur.left,cur_route)
            if cur.right: dfs(cur.right,cur_route)
        dfs(root,[])
        for i in reversed(dic[p]):
            for j in reversed(dic[q]):
                if i==j: return i


root = TreeNode(6)
node1 = TreeNode(2)
node2 = TreeNode(8)
root.left = node1
root.right = node2

s=Solution()
print(s.lowestCommonAncestor(root,node1,node2).val)


###############
#잘못됨 리스트가 shallow copy되는듯
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {}
        def dfs(cur,route):
            route.append(cur)
            dic[cur] = route
            if cur.left: dfs(cur.left,route)
            if cur.right: dfs(cur.right,route)
        dfs(root,[])
        for i in reversed(dic[p]):
            for j in reversed(dic[q]):
                if i!=j: return j

#######################
# 다른사람 풀이
# BST이므로 루트부터 내려와서 두 수의 가운데에 끼는 첫 노드가 LCA가 된다 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low = min(p.val,q.val)
        high = max(p.val,q.val)

        while root:
            if root.val > high:
                root = root.left
            elif root.val < low:
                root = root.right
            else:
                return root