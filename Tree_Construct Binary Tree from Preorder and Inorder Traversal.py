# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# preorder을 통해 root를 알수있고 이를 inorder에서 찾으면 그걸 기준으로 트리를 좌우 양분할수있음
# 만약 좌트리가 있다면 preorder의 다음값은 좌트리의 root
# 이를 이용해 inorder를 양분하는 작업을 반복하다가 

# 공식풀이 나중에 다시보기
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left,right):
            nonlocal preorder_idx
            if left > right: return None
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)

            preorder_idx +=1

            root.left = array_to_tree(left, inorder_index_map[root_val] -1)
            root.right = array_to_tree(inorder_index_map[root_val]+1, right)

            return root

        preorder_idx = 0
        inorder_index_map = {}
        for i, value in enumerate(inorder):
            inorder_index_map[value] = i
        
        return array_to_tree(0, len(preorder)-1)


##########################
#다른사람 풀이
class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])
			
            return root
