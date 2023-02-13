# 릿코드 노드 주어지는 방식은 무슨 방식인지 도저히 이해가 안됨
# 알고리즘에서 막히는게 아니라 맨날 테스트 케이스의 형태랑 함수가 안맞아서 에러뜸


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


class Solution:
    def reverseList(self, head):
        if not head or not head.next: return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur