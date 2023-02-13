#O(log n)안에 해결해야된다고 하니 일단 O(NlogN) 머지소트는 아님, min도 O(N)이라 안됨
#아마 정렬의 일부를 직접 구현하면 될거 같으니 투포인터로 해봄
#풀고보니 이건 투포인터가 아니라 이분탐색인듯 O(logN)

class Solution:
    def findMin(self, nums) -> int:
        st=0
        en=len(nums)-1

        if nums[st] > nums[en]:
            st, en = en, st
        while True:
            mid = (st+en)//2
            if nums[mid] > nums[en]:
                en = mid
            elif nums[mid] <nums[st]:
                st = mid
            else:
                return nums[st]
s=Solution()
print(s.findMin([4,5,6,7,0,1,2]))