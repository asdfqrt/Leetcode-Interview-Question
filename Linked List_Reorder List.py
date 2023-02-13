# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.rev = []
        self.dfs(head)
        nxt = None
        prev = None
        cnt  = 0

        while True:
            nxt = head.next
            if self.rev[cnt] == head or self.rev[cnt]==prev:
                head.next = None
                break
            head.next = self.rev[cnt]
            head.next.next = nxt

            prev = head
            head = nxt
            cnt+=1

        

    def dfs(self, cur):
        if cur.next:
            self.dfs(cur.next)
        self.rev.append(cur)