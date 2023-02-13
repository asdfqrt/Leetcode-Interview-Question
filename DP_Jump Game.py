#다음칸 방문 가능은 list[x] +  x 
#vis[n] =True에서 성공


class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        vis = [True] + [False]*(n+max(nums))
        for i in range(n):
            if vis[i]:
                vis[i+1:i+nums[i]+1] = [True] * nums[i]
        return vis[n-1]


s = Solution()
s.canJump(nums =[2,0])

# 되긴하는데 너무 느림

class Solution:
    # def __init__(self):
    #     self.vis=[]
    def canJump(self, nums) -> bool:
        n = len(nums)
        self.nums = nums
        self.vis = [True]  + [False] * (n-1)
        self.dfs(0,n)
        return self.vis[n-1]
        
    def dfs(self, cur, n):
        self.vis[cur] = True
        for dir in range(1,self.nums[cur]+1):
            if cur + dir < n and not self.vis[cur+dir]: self.dfs(cur + dir, n)

s = Solution()
s.canJump(nums =[2,1,3,1,1])
s.canJump(nums =[2,0])

# dfs 사용해서 처음이랑 연결된 부분만 방문 +  한번 방문했으면 안 방문하는게 나을듯
# TLE 뜸

from collections import deque
class Solution:
    def canJump(self, nums) -> bool:
        q = deque([])
        n = len(nums)
        vis = [True] + [False] *(n-1)
        q.append(0)
        while q:
            cur = q.popleft()
            if cur + nums[cur] >= n-1: return True   
                #여기에 vis = True하면 같은칸이 여러번 q에 들어갈수있음
            for dir in range(1,nums[cur]+1):
                if not vis[cur+dir]:
                    vis[cur+dir] = True
                    q.append(cur+dir)
        return False

#vis 다 확인시 TLE뜸 nums[i] = 10^5숫자고 nums가 10^4개이므로 최악의 경우 nums = [10^5,0,...,0,0,0,0]인 경우 10^5개의 q넣고 확인> 딱히 문제없는데


class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

s = Solution()
s.canJump([2,3,1,1,4])

#이게 맞는듯 목적지에서 역순으로 출발해서 goal까지 오면 된다> goal-nums[x]까지 오면된다 >...>0까지 오면된다 

class Solution:
    def canJump(self, nums) -> bool:
        max_position = 0
        n = len(nums)
        for i in range(n):
            if i<= max_position:
                max_position = max(max_position,i+nums[i])
        return max_position >= n-1

# 이게 더 직관적, O(N)이고 출발지에서 시작해서 최대 뜀거리 안에 있으면(갈수있는 칸이면) 최대 뜀거리를 갱신해주기