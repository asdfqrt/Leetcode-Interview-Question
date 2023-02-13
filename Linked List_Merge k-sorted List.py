from heapq import heappush, heappop
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Wrapper():    #heapq에 [node.val,node]로 넣어도 두번째꺼도 대소관계를 비교해버리기 떄문에(노드끼리는 대소관계 비교불가) wrapper라는 클래스로 묶어서 대소관계비교시 val로 비교하라는 lt시 판정을 따로 지정필요
    def __init__(self,node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap= []
        cur = dummy = ListNode()
        for i in lists:
            if not i: continue  #[[], [1,2,3], [1,2]] 일 경우 []도 i에 들어가기 때문에 heap에 None이 들어감 >> 노드 안나옴
            heappush(heap,Wrapper(i))
        while heap:
            node = heappop(heap).node
            if node.next:
                heappush(heap,Wrapper(node.next))
            cur.next = node
            cur = cur.next
        return dummy.next


