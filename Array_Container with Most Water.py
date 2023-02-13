#dp, 투포인터, 파라매트릭 서치
# class Solution:
#     def maxArea(self, height) -> int:
#         st=0
#         en = len(height)-1
#         hmax = [height[st],height[en]]
#         smax = (en-st) * min(hmax)
#         for st, startheight in enumerate(height):
#             en = len(height)-1
#             if st>0 and startheight < hmax[0]: continue
#             hmax = [startheight,height[en]]
#             while st<en:
#                 if height[en] >= hmax[1]:
#                     hmax[1] = height[en]
#                     smax = max(smax,(en-st) * min(hmax))
#                 en -= 1
#         return smax






class Solution:
    def maxArea(self, height) -> int:
        st = 0
        en = len(height)-1
        smax = 0
        while st<en:
            smax = max(smax,(en-st) * min(height[st],height[en]))
            if height[st] < height[en]:
                st+=1
            else:
                en-=1
        return smax



s= Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
