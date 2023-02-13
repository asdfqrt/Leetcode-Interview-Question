# 똑같은 DP문제인데 첫집과 끝집 연결되어있음
# nums[0]과 nums[-1] 둘다 털기 x
# 그냥 nums[0]을 터는 dp, nums[0]을 안터는 dp 둘다 만들면 되지않나
# 그럴필요없이 일반 dp만들고 마지막 d를 검사하는 방법은? arr[0]이 사용됫는지 알아야됨 그러면> 두개만드는거랑 다를거 없는듯
# 집 하나일 경우 털수있게 해야됨

class Solution:
    def rob(self, nums) -> int:
        d = [[0,nums[0]]]
        dnot = [[0,0]]
        n = len(nums)
        for i in range(1,n):
            d.append([max(d[i-1][0],d[i-1][1]), d[i-1][0]+nums[i]])
            dnot.append([max(dnot[i-1][0],dnot[i-1][1]), dnot[i-1][0]+nums[i]])
        
        return max(d[-1][0],max(dnot[-1])) if n!=1 else d[-1][1]

s = Solution()
print(s.rob(nums = [1]))
##########################################
#아예 주어지는 리스트를 슬라이싱 해서 함수따로둬서 [1:], [:-1]로 두번실행시키는 방법도 있음, 시간복잡도는 같음
#max(nums[0],solve(nums[1:]),solve(nums[:-1]))
class Solution:
    def solve(self, nums) -> int:
        d = [[0,nums[0]]]
        n = len(nums)
        for i in range(1,n):
            d.append([max(d[i-1][0],d[i-1][1]), d[i-1][0]+nums[i]])
        return max(d[n-1])
    def rob(self, nums) -> int:
        return max(self.solve(nums[1:]),self.solve(nums[:-1])) if len(nums) != 1 else nums[0]
