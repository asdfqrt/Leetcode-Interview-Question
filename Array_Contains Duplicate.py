#length 10^5 << O(N)이면 0.0001이니 충분할듯

class Solution:
    def containsDuplicate(self, nums) -> bool:
        isused = set()
        for i in nums:
            if i in isused:
                return True
            else:
                isused.add(i)
        return False


