#다이나믹 or 투포인터 쓰면되는데 follow up에서 devide and conquer 재귀?도 써보라고함 devide and conquer가 뭔데
#갯수 10^5니까 O(N)이면 0.5초이내


class Solution:
    def maxSubArray(self, nums) -> int:
        d=nums[:] #d[x] = x번째 숫자를 포함하는 부분 행렬 중 최대 합
        for i in range(1,len(nums)):
            d[i] = max(d[i],d[i-1]+nums[i])
        return(max(d))


s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))