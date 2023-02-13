class Solution:
    def longestPalindrome(self, s: str) -> str:
        for pl in range(len(s),0,-1):
            st = 0
            for en in range(pl, len(s)+1):
                if s[st:en] == s[st:en][::-1]:
                    return s[st:en]
                st +=1

s = Solution()
print(s.longestPalindrome("aba"))



######################################
#d[i][j] = [True] Si~Sj가 펠린드롬인가
# d[i][j] = d[i+1][j-1] and Si == Sj 