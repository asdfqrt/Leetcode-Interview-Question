# 거리 구하는것도 아니고 dfs 하면될듯, 그래프 따로 안만들고 배열 도는걸로
# 1 <=m,n <= 200

#dfs 실패
class Solution:
    def pacificAtlantic(self, heights):
        self.heights =heights
        self.nx = [1,0,-1,0]
        self.ny = [0,1,0,-1]
        self.m,self.n = len(heights), len(heights[0])
        self.vis = [[False]*self.n for _ in range(self.m)]
        self.P = set()
        self.A = set()
        ans = []


        for x in range(self.m):
            for y in range(self.n):
                # if not self.vis[x][y]:    이거 넣으면 [[3,3,3],[3,1,3],[0,2,4]] 에서 반례발생
                    self.dfs(x,y)
        return sorted(list(map(lambda x: list(x),self.P & self.A)))
        
    def dfs(self,x,y):

        self.vis[x][y] = True
        for i in range(4):
            dx = x + self.nx[i]
            dy = y + self.ny[i]

            if dx<0 or dy<0 :
                # self.P.add([x,y])       #리스트는 set 안에 들어갈수없음. 문자열, 숫자, 튜플만 가능
                self.P.add((x,y))
            elif dx>=self.m or dy>=self.n:
                self.A.add((x,y))
            elif self.heights[dx][dy] <= self.heights[x][y]:
                if not self.vis[dx][dy]: self.dfs(dx,dy)
                if (dx,dy) in self.P: self.P.add((x,y))
                if (dx,dy) in self.A: self.A.add((x,y))


s = Solution()
# print(s.pacificAtlantic(heights = [[3,3,3],[3,1,3],[0,2,4]]))
# print(s.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(s.pacificAtlantic(heights = [[7,1,17,13,9,10,5,14,0,3],[7,15,7,8,15,16,10,10,5,13],[18,9,15,8,19,16,7,5,5,10],[15,11,18,3,1,17,6,4,10,19],[3,16,19,12,12,19,2,14,5,9],[7,16,0,13,14,7,2,8,6,19],[5,10,1,10,2,12,19,1,0,19],[13,18,19,12,17,17,4,5,8,2],[2,1,17,13,14,12,14,2,16,10],[5,8,1,11,16,1,18,15,6,19],[3,8,14,14,5,0,2,7,5,1],[17,1,9,17,10,10,10,7,1,16],[14,18,5,11,17,15,8,8,14,13],[6,4,10,17,8,0,11,4,2,8],[16,11,17,9,3,2,11,0,6,5],[12,18,18,11,1,7,12,16,12,12],[2,14,12,0,2,8,5,10,7,0],[16,13,1,19,8,13,11,8,11,3],[11,2,8,19,6,14,14,6,16,12],[18,0,18,10,16,15,15,12,4,3],[8,15,9,13,8,2,6,11,17,6],[7,3,0,18,7,12,2,3,12,10],[7,9,13,0,11,16,9,9,12,13],[9,4,19,6,8,10,12,6,7,11],[5,9,18,0,4,9,6,4,0,1],[9,12,1,11,13,13,0,16,0,6],[7,15,4,8,15,17,17,19,15,1],[7,17,4,1,1,14,10,19,10,19],[10,5,12,5,8,8,14,14,6,0],[16,10,10,7,13,4,0,15,18,0],[11,2,10,6,5,13,4,5,3,1],[9,14,16,14,15,3,2,13,17,8],[19,2,10,1,2,15,12,10,2,5],[12,4,8,9,8,6,4,14,14,0],[11,17,17,4,16,13,6,15,5,7],[12,18,1,3,9,10,7,1,1,1],[18,6,10,8,12,14,9,12,10,3],[15,13,18,13,8,5,12,14,18,0],[15,4,8,9,19,18,6,19,12,0],[4,14,15,4,17,17,9,17,9,0],[6,17,16,10,3,8,8,18,15,9],[3,8,4,2,13,0,2,8,8,2],[14,12,13,12,17,4,16,9,8,7],[0,19,8,16,1,13,7,6,15,11],[1,13,16,14,10,4,11,19,9,13],[8,0,2,1,16,12,16,9,9,9],[5,2,10,4,8,12,17,0,2,15],[11,2,15,15,14,9,11,19,18,11],[4,4,1,5,13,19,9,17,17,17],[4,1,8,0,8,19,11,0,5,4],[8,16,14,18,12,2,0,19,0,13],[7,11,3,18,8,2,2,19,8,7],[3,13,6,1,12,16,4,13,0,5],[12,1,16,19,2,12,16,15,19,6],[1,7,12,15,3,3,13,17,16,12]]))
###############################

from collections import deque
class Solution:
    def pacificAtlantic(self, heights):
        self.heights =heights
        self.nx = [1,0,-1,0]
        self.ny = [0,1,0,-1]
        self.m,self.n = len(heights), len(heights[0])
        self.vis = [[False]*self.n for _ in range(self.m)]
        self.P = set()
        self.A = set()
        ans = []
        q = deque([])


        for x in range(self.m):
            for y in range(self.n):
                if self.vis[x][y]: continue
                self.vis[x][y] = True
                q.append([x,y])
                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        dx = x + self.nx[i]
                        dy = y + self.ny[i]
                        if dx<0 or dy<0 :
                            self.P.add((x,y))
                        elif dx>=self.m or dy>=self.n:
                            self.A.add((x,y))
                        elif self.heights[dx][dy] <= self.heights[x][y]:
                            if not self.vis[dx][dy]:
                                self.vis[dx][dy] = True
                                q.append([dx,dy])
    
        return sorted(list(map(lambda x: list(x),self.P & self.A)))

# 모든 노드에서 bfs 확인 방식으로는 도달이후에 도달까지의 경로상에 있던 모든 점들이 도달가능이라는걸 상위노드에 알릴수 없는듯?
# 재귀 dfs는 경로가 저장되니 될거 같은데 자꾸 반례가 나옴
# 할꺼면 바다 변에서 스타트 지점을 잡아야할듯 그래야 처음부터 A나 P라는 정보를 가지고 top down전달가능

###################################

class Solution:
    def pacificAtlantic(self, heights):
        self.heights = heights
        self.nx = [1,0,-1,0]
        self.ny = [0,1,0,-1]
        self.m,self.n = len(heights), len(heights[0])
        self.vis_P = [[False]*self.n for _ in range(self.m)]
        self.vis_A = [[False]*self.n for _ in range(self.m)]

        Pac = True
        Atl = False
        
        for x in range(self.m):
            for y in range(self.n):
                if x==0 or y==0:
                    # if self.vis_P[x][y]: continue   # if만 나가야되는데 for문 전체 나가서 0,self.n-1이 실행이 안됨
                    if not self.vis_P[x][y]: self.dfs(x,y,Pac)
                if x==self.m-1 or y == self.n-1:
                    if not self.vis_A[x][y]: self.dfs(x,y,Atl)
        ans = []
        for x in range(self.m):
            for y in range(self.n):
                if self.vis_P[x][y] and self.vis_A[x][y]:
                    ans.append([x,y])
        return ans
        
    def dfs(self,x,y,ocean):
        if ocean: self.vis_P[x][y] = True
        else: self.vis_A[x][y] = True

        for i in range(4):
            dx = x + self.nx[i]
            dy = y + self.ny[i]
            if 0<=dx<self.m and 0<=dy<self.n and self.heights[dx][dy] >= self.heights[x][y]:
                if ocean:
                    if not self.vis_P[dx][dy]: self.dfs(dx,dy,ocean)
                else:
                    if not self.vis_A[dx][dy]:self.dfs(dx,dy,ocean)

s = Solution()
# print(s.pacificAtlantic(heights = [[3,3,3],[3,1,3],[0,2,4]]))
# print(s.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(s.pacificAtlantic(heights = [[7,1,17,13,9,10,5,14,0,3],[7,15,7,8,15,16,10,10,5,13],[18,9,15,8,19,16,7,5,5,10],[15,11,18,3,1,17,6,4,10,19],[3,16,19,12,12,19,2,14,5,9],[7,16,0,13,14,7,2,8,6,19],[5,10,1,10,2,12,19,1,0,19],[13,18,19,12,17,17,4,5,8,2],[2,1,17,13,14,12,14,2,16,10],[5,8,1,11,16,1,18,15,6,19],[3,8,14,14,5,0,2,7,5,1],[17,1,9,17,10,10,10,7,1,16],[14,18,5,11,17,15,8,8,14,13],[6,4,10,17,8,0,11,4,2,8],[16,11,17,9,3,2,11,0,6,5],[12,18,18,11,1,7,12,16,12,12],[2,14,12,0,2,8,5,10,7,0],[16,13,1,19,8,13,11,8,11,3],[11,2,8,19,6,14,14,6,16,12],[18,0,18,10,16,15,15,12,4,3],[8,15,9,13,8,2,6,11,17,6],[7,3,0,18,7,12,2,3,12,10],[7,9,13,0,11,16,9,9,12,13],[9,4,19,6,8,10,12,6,7,11],[5,9,18,0,4,9,6,4,0,1],[9,12,1,11,13,13,0,16,0,6],[7,15,4,8,15,17,17,19,15,1],[7,17,4,1,1,14,10,19,10,19],[10,5,12,5,8,8,14,14,6,0],[16,10,10,7,13,4,0,15,18,0],[11,2,10,6,5,13,4,5,3,1],[9,14,16,14,15,3,2,13,17,8],[19,2,10,1,2,15,12,10,2,5],[12,4,8,9,8,6,4,14,14,0],[11,17,17,4,16,13,6,15,5,7],[12,18,1,3,9,10,7,1,1,1],[18,6,10,8,12,14,9,12,10,3],[15,13,18,13,8,5,12,14,18,0],[15,4,8,9,19,18,6,19,12,0],[4,14,15,4,17,17,9,17,9,0],[6,17,16,10,3,8,8,18,15,9],[3,8,4,2,13,0,2,8,8,2],[14,12,13,12,17,4,16,9,8,7],[0,19,8,16,1,13,7,6,15,11],[1,13,16,14,10,4,11,19,9,13],[8,0,2,1,16,12,16,9,9,9],[5,2,10,4,8,12,17,0,2,15],[11,2,15,15,14,9,11,19,18,11],[4,4,1,5,13,19,9,17,17,17],[4,1,8,0,8,19,11,0,5,4],[8,16,14,18,12,2,0,19,0,13],[7,11,3,18,8,2,2,19,8,7],[3,13,6,1,12,16,4,13,0,5],[12,1,16,19,2,12,16,15,19,6],[1,7,12,15,3,3,13,17,16,12]]))
