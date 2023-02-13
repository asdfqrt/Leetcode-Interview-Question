#중앙을 원점으로 하고 (x,y) > (-x,y) 등으로 선대칭? 각사분면마다 다른거 곱해야되서 귀찮을듯

class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for st in range(n//2):
            for i in range(n-(st*2)-1):           
                # matrix[st][st+i]
                # matrix[st+i][n-1-st]
                # matrix[n-1-st][n-1-st-i]
                # matrix[n-1-st-i][st]
                matrix[st][st+i],matrix[st+i][n-1-st],matrix[n-1-st][n-1-st-i],matrix[n-1-st-i][st] = matrix[n-1-st-i][st],matrix[st][st+i],matrix[st+i][n-1-st],matrix[n-1-st][n-1-st-i]

###################
# 좀더 좋은풀이 >> 행과 열을 바꾼 전치행렬 Transpose를 구하고 이를 y역순으로 뒤집기
# 시간복잡도는 더 크지만 코드간결, numpy등 빌트인 함수 사용가능

class Solution:
    def rotate(self, matrix) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    def reflect(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s= Solution()
s.rotate(matrix)
print(matrix)
