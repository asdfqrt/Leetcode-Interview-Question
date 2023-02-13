#DP도 되겟지만 콤비네이션 쓰면 개빨리 풀릴듯?
#d[x][y] = (x,y)까지 오는 루트 가짓수 로하거나
# d[x] = x번째 이동으로 만들수있는 가짓수
# m,n 주머니에서 고르는거고 선택하는 가짓수 고르면될듯
# 세로 m-1 + 가로 n-1 총 m+n-2번 이동하고 이중 세로를 언제언제 이동할거냐 m+n-2 C m-1

from  itertools import combinations
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return len(list(combinations(range(m+n-2),m-1)))

s = Solution()
print(s.uniquePaths(m = 3, n = 7))

# combinatino쓰니까 TLE 나서 못씀

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1]*n for _ in range(m)]

        for x in range(1,m):
            for y in range(1,n):
                d[x][y] = d[x-1][y]+d[x][y-1]   #x,y까지 이동하는 가짓수; d[x][y] = d[x-1][y]+d[x][y-1]
        return d[-1][-1]


from math import factorial as f #nCm 조합 리스트를 다 구하는거 말고 숫자만 계산하는건 생각보단 빠른듯? 그래도 dp가 더빠르네
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        return f(m+n-2) // (f(m-1) * f(n-1)) 
s = Solution()
print(s.uniquePaths(m = 3, n = 7))