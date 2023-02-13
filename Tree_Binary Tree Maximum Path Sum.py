# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# 각 노드 dic에 다른가지와 아직 안합쳐서 합칠수 있을때의 최대(안꺾은), 안꺾은 + 다른 가지랑 합쳐서 이미 완성되어버린(꺾은) 최대  둘다 저장
# ㄴㄴ 반환만 해주면 됨 위로 
# 루트에서 비교

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dic = {}
        inf = float("inf")
        def dfs(cur):
            l,r,fl,fr =-inf,-inf,-inf,-inf
            if cur.left:
                l,fl = dfs(cur.left)
            if cur.right:
                r,fr = dfs(cur.right)
            ans1 = max(cur.val,cur.val+l,cur.val+r)
            ans2 = max(ans1,cur.val+l+r,fl,fr)
            # dic[cur] = (ans1,ans2)
            return (ans1,ans2)
        return dfs(root)[1]
        # return max(dic[root])


######################
# 공식해설, ans2를 저장해서 올리지 않고 꺾는 지점 마다 ans2값을 갱신, 이러면 못꺾는 fl,fr을 따로 저장할필요가 없음
class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path

            if not node:
                return 0

            gain_from_left = max(gain_from_subtree(node.left), 0)

            gain_from_right = max(gain_from_subtree(node.right), 0)

            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)
        return max_path