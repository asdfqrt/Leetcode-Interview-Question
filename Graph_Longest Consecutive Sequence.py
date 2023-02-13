#LCS
# O(N)에 동작해야 되고 기존DP LCS랑 다르게 주어진 배열이 연속해있지않은데 
# d[x]=x자리까지 봣을때 연속된 배열의 길이 >>d[x-1]이 d[x]에 영향을 못줌 >> dp로는 못푸는듯
# vis = {} 로 두고 숫자가 처음들어오면 숫자+1,-1방향으로 탐사해서 끝까지 감
# 끝까지 간 숫자에서 연속이 끝나면 1리턴, 그 상위 함수가 1+1, 그상위가ㅣ 1+1+1>>
# vis = {100:1, 4:4, 3:3, 2:2, 1:1, 200:1,} 로 갱신
# 함수위로 올라올때 max값도 갱신 >> 그냥 마지막에 해도 + O(N) 이라 차이 없을듯

class Solution:
    def longestConsecutive(self, nums) -> int:
        self.vis = {i:0 for i in nums}
        for num in nums:
            if self.vis[num]==0:
                self.dfs(num)
        return max(self.vis.values()) if self.vis else 0    #nums가 []일경우

    def dfs(self, cur):
        self.vis[cur] = 1
        for i in [-1,1]:
            dx = cur + i
            if dx in self.vis and self.vis[dx] == 0:
                self.vis[cur] += self.dfs(dx)
        return self.vis[cur]

s= Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))