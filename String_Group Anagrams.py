#https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        copy = strs.copy()
        n = len(strs)
        exist = defaultdict(list)
        for i in range(n):
            copy[i] = ''.join(sorted(copy[i]))
            exist[copy[i]].append(strs[i])
        return list(exist.values())

##########################
class Solution(object):
    def groupAnagrams(self, strs):
        exist = defaultdict(list)
        for string in strs:
            exist[tuple(sorted(string))].append(string)
        return list(exist.values())
##########################
class Solution:
    def groupAnagrams(self,strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


s = Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
        
