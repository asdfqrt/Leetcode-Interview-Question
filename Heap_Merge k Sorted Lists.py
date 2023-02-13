# https://leetcode.com/problems/merge-k-sorted-lists/
# 전에 푼거
from heapq import heappush, heappop
class Wrapper():
    def __init__(self,node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap= []
        cur = dummy = ListNode()
        for i in lists:
            if not i: continue
            heappush(heap,Wrapper(i))
        while heap:
            node = heappop(heap).node
            if node.next:
                heappush(heap,Wrapper(node.next))
            cur.next = node
            cur = cur.next
        return dummy.next