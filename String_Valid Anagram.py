# https://leetcode.com/problems/valid-anagram/
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# 유니코드도 set에 들어가지 않나?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        exist = {}
        for string in t:
            exist[string] = exist.get(string, 0)+1
        for string in s:
            if string not in exist or exist[string]==0: return False
            exist[string] -=1
        return max(exist.values())==0

###############
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


##############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)