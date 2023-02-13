#https://leetcode.com/problems/minimum-window-substring/
#Follow up: Could you find an algorithm that runs in O(m + n) time?
# 투포인터 쓰면 O(m)에 dic에 기록, O(n)에 탐색 가능
# 처음부터  dic 0되는 시점까지 탐색, 이후 st를 dic 까지 끌어올림 반복
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        exist = {}
        for string in t:
            exist[string] = exist.get(string, 0) + 1
        n = len(s)
        st = 0
        en = 0
        ans = [0,float("inf")]
        while en != n:
            string = s[en]
            if string in exist:
                exist[string] -= 1
            if max(exist.values()) <= 0:
                if ans[1]-ans[0] > en-st: ans = [st,en] 
                if s[st] in exist: exist[s[st]]+=1
                st +=1
                while st<=en and s[st] not in exist:
                    st+=1
                exist[string] += 1
            else:
                en+=1
        return s[ans[0]:ans[1]+1] if ans[1] != float("inf") else ""

s= Solution()
print(s.minWindow(s = "cabwefgewcwaefgcf", t = "cae"))
print(s.minWindow(s = "ab", t = "a"))
print(s.minWindow(s = "a", t = "aa"))
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))



