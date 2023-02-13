from collections import deque
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        q = deque([])
        for i in range(n):
            q.append((i,i))
            q.append((i,i+1))
            while q:
                st,en = q.popleft()
                if st >=0 and en <n and s[st] == s[en]:
                    cnt+=1
                    q.append((st-1,en+1))
        return cnt
s = Solution()
print(s.countSubstrings("aba"))