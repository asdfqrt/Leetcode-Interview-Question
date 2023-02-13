# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
# 자주 바뀌는 경우는 c++ stl의 ordered set이나 ordered multiset 같은거 사용해야됨
# avl이나 r-b 자가균형트리를 구현하고 이를 리스트화 해야되기때문에 파이썬에선 사실상 불가능
# 자가 균형트리에 삽입을 하는 nlogn까진 괜찮아도 인덱스 k를 통해 접근하기 위해 리스트화 할때 O(N) 되버림>> 걍 sort하는것보다 느려
# 최선의 경우가 리스트화 안하고 그냥 for 걸어서 k번째 찾는 O(k)일듯, 최종으로 O(NlogN +k)
# 파이썬으로 굳이 구현한다면 heapq로 자료 받은다음 k번째까지 heappop해내고 다시 빼낸거 heappush하면될듯

# 공식 해설에서는 리스트화 하지않고 double linked list화 해두었다가 insert/del한다고
# 하지만 linkedlist면 삽입삭제하려면 root 부터 쭉 따라가야되는데 그럼 한번 삽입할때마다 트리에서 O(logN)+ linkedlist에서 O(N)인데 검색만 O(k)지 나머지는 다 느림

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        def dfs(cur):
            order.append(cur.val)
            if cur.left: dfs(cur.left)
            if cur.right: dfs(cur.right)
        dfs(root)
        order.sort()
        return order[k-1]