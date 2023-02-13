#전형적인 DP문제
#d[x] = x까지 오는경우의 수면
#d[x] = d[x-1] + d[x-2] 한칸전에서 한칸오르는경우 + 한칸전에서 두칸오르는경우

class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0,1,2]
        for i in range(3,n+1):
            d.append(d[i-1] + d[i-2])
        return d[n]

