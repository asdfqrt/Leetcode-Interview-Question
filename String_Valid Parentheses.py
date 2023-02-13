#https://leetcode.com/problems/valid-parentheses/
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque([])
        open = {")": "(", "]":"[", "}":"{"}
        for string in s:
            if string not in open:
                q.append(string)
            else:
                if not q or open[string] != q.pop(): return False
        return not q