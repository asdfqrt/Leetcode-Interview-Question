#https://leetcode.com/problems/longest-repeating-character-replacement/
# s길이 10^5, O(N)정도에 풀어야될듯 매 문자에서 출발하여 확인하는 방법은 O(N^2)ㄴㄴㄴㄴ
# 근데 딱히 생각이 안나는걸, 투포인터?
##############
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = 0
        exist = defaultdict(int)
        ans = 0
        for en,string in enumerate(s):
            exist[string] += 1
            max_idx = max(exist,key=exist.get)
            while (en-st+1)-exist[max_idx] > k:
                exist[s[st]] -= 1
                st +=1
                max_idx = max(exist,key=exist.get)
            ans = max(ans,en-st+1)
        return ans

###################
# 간격을 한번만 줄이면 매 시행마다 exist내에 있는 최대 문자가 무엇인지 찾지 않아도 된다

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = 0
        exist = {}
        max_freq = 0
        ans = 0
        for en,string  in enumerate(s):
            exist[string] = exist.get(string, 0) + 1    #defaultdic 대신 쓸수있음
            max_freq = max(max_freq, exist[string])
            if (en-st+1) - max_freq > k:    # 간격에서 최대 빈도 빼면 그게 나머지의 빈도의 합
                exist[s[st]] -= 1   # 한번 정해진 ans 간격을 줄이지 않고 딱 한번만 st를 제거하고 넘어감,  그걸로 안되면 어짜피 답 아님
                st += 1

            ans = en-st +1   

        return ans





s = Solution()
# print(s.characterReplacement("ABBB",2))
# print(s.characterReplacement("ABAB",2))
print(s.characterReplacement(s = "AABABBA", k = 1))



