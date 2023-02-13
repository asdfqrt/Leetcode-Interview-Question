# 백준의 그림과 동일문제

class Solution:
    def numIslands(self, grid) -> int:
        self.m,self.n = len(grid),len(grid[0])
        self.vis = set()
        self.grid = grid
        self.nx = [1,0,-1,0]
        self.ny = [0,1,0,-1]
        cnt = 0
        for x in range(self.m):
            for y in range(self.n):
                if (x,y) in self.vis or grid[x][y]=="0": continue
                cnt +=1
                self.dfs(x,y)
        return cnt

    def dfs(self,x,y):
        self.vis.add((x,y))
        for i in range(4):
            dx = x + self.nx[i]
            dy = y + self.ny[i]
            if 0<=dx<self.m and 0<=dy<self.n and self.grid[dx][dy]=="1" and (dx,dy) not in self.vis:
                self.dfs(dx,dy)
s = Solution()
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))