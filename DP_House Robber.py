#전형적인 DP문제
#d[x] = [이전house가 털렸을때 x까지 턴 최대액수,이전house가 안털렸을때 기준 x 집까지 최대액수]
#d[x] = [x번째 집 안 턴경우, x번째집 턴 경우]
#d[x] = [ max(d[x-1][0],d[x-1][1]) , d[x-1][0]+arr[x] ]
class Solution:
    def rob(self, nums) -> int:
        d = [[0,nums[0]]]
        n = len(nums)
        for i in range(1,n):
            d.append([max(d[i-1][0],d[i-1][1]), d[i-1][0]+nums[i]])
        return max(d[n-1])
s = Solution()
print(s.rob(nums = [2,7,9,3,1]))


############################
class Solution:
    def rob(self, nums: List[int]) -> int:
        to_rob,not_to_rob = 0,0
        
        for i in nums:
            temp = max(i+to_rob , not_to_rob)
            
            to_rob = not_to_rob
            not_to_rob = temp
        return not_to_rob
# 이 방식대로 하면 리스트d를 만들필요가 없어서 좀 더 메모리 사용량이 적긴할듯