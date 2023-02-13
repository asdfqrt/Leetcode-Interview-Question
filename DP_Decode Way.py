#DP
# d[x][0] = 앞자리와 합쳤을때 해독가짓수, d[x][1] = 앞자리와 안 합쳤을때 해독가짓수
# d[x][0] = d[x-1][1]
# d[x][1] = d[x-1][0] + d[x-1][1]
# 앞자리와 합치고 못합치고의 기준; 두자리>26 or 두자리 <10 x, 현자리 0 무조건 합침 
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s[0] == "0": return 0
#         d = [[0,1]]
#         for i in range(1,len(s)):
#             two = int(s[i-1]+s[i])
#             d.append([d[i-1][1],sum(d[i-1])])
#             if two > 26 or two < 10:
#                 d[i][0] = 0
#             if s[i] == "0":
#                 d[i][1] = 0
#         return (sum(d[-1]))

                

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        d = [0] * (len(s)+1)
        d[0] = 1
        d[1] = 1
        for i in range(2,len(s)+1):
            two = int(s[i-2] +s[i-1])
            if 10 <= two <= 26 :
                d[i] += d[i-2]
            if s[i-1] != "0":
                d[i] += d[i-1]
        return d[-1]
# 그냥 초깃값 전부 0으로 설정해놓고 0이 아닐때 앞자리와 무관하게 [ ] + 현숫자 로 추가가능하니 d[i-1]받아오고
# 앞자리까지 합해서 10~26 사이이면 두자리 합하는거 가능하니 [  ] + 두자리 가능해서 d[i-2]도 추가하는 방법





s = Solution()
s.numDecodings(s = "12")
s.numDecodings(s = "0")
s.numDecodings(s = "2101")
s.numDecodings(s = "100")
