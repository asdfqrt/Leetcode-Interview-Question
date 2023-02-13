#전형적인 DP문제인듯
#d[x] = x번째 글자까지 s내에서 해결할수있냐
#d[x] = d[x-(dic내의 글자길이)] =True and s[x-(dic내의 글자길이):x] =  (dic내의 글자)

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        d=[True]
        for i in range(1,len(s)+1):
            d.append(False)
            for j in wordDict:
                if i>=len(j) and d[i-len(j)] == True and s[i-len(j):i] == j:
                    d[i] = True
                    break
        # return "true" if d[len(s)] else "false"
        return d[len(s)]



s= Solution()
print(s.wordBreak( s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
print(s.wordBreak("leetcode", wordDict = ["leet","code"]))