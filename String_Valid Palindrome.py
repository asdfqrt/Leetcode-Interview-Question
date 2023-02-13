# 그냥 큐넣고 팝 레이프트밥 해서 비교하면될듯

from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque([])
        for string in s.lower():
            if string.isalnum():
                q.append(string)
        while len(q)>1:
            l = q.popleft()
            r = q.pop()
            if l!=r:
                return False
        return True

s = Solution()
print(s.isPalindrome("0P"))

###########################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for string in s.lower():
            if string.isalnum():
                ans +=string
        return s == ans[::-1]