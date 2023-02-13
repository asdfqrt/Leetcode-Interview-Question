# https://leetcode.com/problems/set-matrix-zeroes/
# in place > 추가 저장소를 사용하지 않고 하기
# bfs는 큐 사용하기에 불가? 재귀 dfs도 vis써야되는데
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# constant space solution이 있다

# O(mn)은 vis 배열을 사용하는 dfs 방법내지 새로운 배열 만들어서 붙여넣기
# O(m+n)은 s0이 있는 x, 0이 있는 y좌표를 두 set에 각각 넣는 방법
# O(1) space는 뭐지? 탐색자체를 한줄씩? string 문자열에 공백구분같은걸로 한 문자안에 좌표값여럿저장?
# 행렬의 좌, 상단을 인덱스로 쓰는 방법
# x,y의 좌표값이 0이면 matrix[x][0] =0, matrix[0][y] = 0
# 이후 행렬 인덱스를 제외한 모든 칸을 한칸씩 방문하며 이 둘중 하나라도 0이면 그칸을 0으로 채움
####
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_x = set()
        zero_y = set()
        m = len(matrix)
        n = len(matrix[0])
        isCol =False
        isRow =False


        for x in range(m):
            if matrix[x][0] ==0:
                isCol = True
        for y in range(n):
            if matrix[0][y]==0:
                isRow = True

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0
        for x in range(1,m):
            for y in range(1,n):
                if matrix[x][0]==0 or matrix[0][y]==0:
                    matrix[x][y] =0

        if isCol:
            for x in range(m):
                matrix[x][0]=0
        if isRow:
            for y in range(n):
                matrix[0][y]=0


###################
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_x = set()
        zero_y = set()
        m = len(matrix)
        n = len(matrix[0])
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    zero_x.add(x)
                    zero_y.add(y)
        for x in range(m):
            for y in range(n):
                if x in zero_x or y in zero_y:
                    matrix[x][y] = 0


s = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print(matrix)

###############

