#nlogn은 쉬우니까 O(n)으로 하기?
#STL 안쓰고 풀기
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            arr.append(bin(i).count("1"))
        return arr