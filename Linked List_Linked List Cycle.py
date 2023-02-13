# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.vis = set()
    def hasCycle(self, head) -> bool:
        self.vis.add(head)
        if not head or not head.next: return False
        if head.next in self.vis : return True
        return self.hasCycle(head.next) 