#https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = deque([])
        exist = set()
        longest = 0
        for string in s:
            if string not in exist:
                exist.add(string)
                cur.append(string)
            else:
                longest = max(longest,len(cur))
                while cur[0] != string:
                    exist.remove(cur.popleft())
                cur.popleft()
                cur.append(string)
        return max(longest,len(cur))



###########################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist = {}
        ans = 0
        st = 0
        for en,string in enumerate(s):
            if string in exist:
                st = max(st,exist[string]+1)
            exist[string] = en
            ans = max(ans,en-st+1)
        return ans



s = Solution()
print(s.lengthOfLongestSubstring("abba"))
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring(" "))