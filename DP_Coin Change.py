#그리디 +DP인거 같음
#d[x] = x숫자를 나타내는 코인 최소갯수
#x=1~amount까지 큰 코인부터 주면될듯

import sys
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        d = [0]+[sys.maxsize]*(amount)
        for i in coins: #최대 O(12)
            for j in range(i,amount+1): #O(12) * O(10^4)
                d[j] = min(d[j-i]+1,d[j])
        return d[amount] if d[amount] != sys.maxsize else -1

#굳이 큰 코인부터 셀 필요 없었음

s=Solution()
print(s.coinChange(coins = [1,2,5], amount = 11))
print(s.coinChange(coins = [2], amount = 3))
print(s.coinChange(coins = [1], amount = 0))