#길이가 10^4, O(N^2)까지 1초내에 가능

class Solution:
    def maxProduct(self, nums) -> int:
        d=[[nums[0],nums[0]]]
        for i in range(1,len(nums)):    #O(N)
            d.append([max(d[i-1][0] * nums[i], d[i-1][1] * nums[i], nums[i]),min(d[i-1][0] * nums[i], d[i-1][1] * nums[i], nums[i])])
        return max(d)[0]


# s=Solution()
# print(s.maxProduct([-2,3,-2,0,-4,5,5,-4]))