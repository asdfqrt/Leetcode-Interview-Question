# 리트코드의 문제에서는 입력을 binary string으로 주겠다고 했지만 실제로 run 돌려보면 함수에 들어오는 값은 int라서 문제 생겼엇음


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


