class Solution:
    def spiralOrder(self, matrix) -> List[int]:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.nx = [0,1,0,-1]    #right, down, left, up priority
        self.ny = [1,0,-1,0]
        self.vis = [[False]*self.n for _ in range(self.m)]
        self.path = []
        
        
        self.dfs(0,0,0)
        return self.path
    def dfs(self,x,y,dir):
        self.vis[x][y] = True
        self.path.append(self.matrix[x][y])
        dx = x + self.nx[dir]
        dy = y + self.ny[dir]
        if 0<=dx<self.m and 0<=dy<self.n and not self.vis[dx][dy]:
            self.dfs(dx,dy,dir)
        else:
            for dir in range(4):
                dx = x + self.nx[dir]
                dy = y + self.ny[dir]
                if 0<=dx<self.m and 0<=dy<self.n and not self.vis[dx][dy]:
                    self.dfs(dx,dy,dir)

#####################
#이것도 괜찮은듯, 다음칸이 막혔을때를 기준으로 방향꺾기, 탐색의 끝은 m*n번 돌면 끝
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 0,1 -> 1,0 -> 0,-1 -> -1,0 -> 0,1.  dx, dy = dy, -dx
        # if any checked elements or outside the border, change the path

        m = len(matrix)
        n = len(matrix[0])
        #start point
        x = y = 0
        #start path
        dx, dy = 0, 1
        #output array
        res = []
        #run through the board
        for _ in range(m*n):
            res.append(matrix[x][y])
            matrix[x][y] = '*'
            if not 0<=x+dx<m or not 0<=y+dy<n or matrix[x+dx][y+dy]=='*':
                dx, dy = dy, -dx
            x += dx
            y += dy        
        return res
