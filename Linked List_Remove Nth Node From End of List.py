# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.cnt = 0
        self.temp = None
        self.dfs(head,n)
        return head if head != self.temp else head.next

    def dfs(self,head,n):
        if head.next:
            self.dfs(head.next,n)
        self.cnt +=1
        if self.cnt==n:
            self.temp = head
        elif self.cnt==n+1:
            head.next = self.temp.next