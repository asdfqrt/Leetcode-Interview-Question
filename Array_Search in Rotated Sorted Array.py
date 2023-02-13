#target의 index를 찾으라는건데 이것도 이분탐색으로 하면될듯. 첫 이분탐색으로 정렬하고 두번쨰 이분탐색으로 찾으면딜듯

class Solution:

    def search(self, nums, target: int) -> int:
        pivot = self.findMin(nums)
        n = len(nums)
        st = 0
        en = n-1
        while st<=en:
            mid = (st+en)//2
            realmid = (mid+pivot)%n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                st = mid+1
            else:
                en = mid-1
        return -1
        
        # new = nums[pivot:] + nums[:pivot] # new라는 새 리스트를 슬라이싱으로 만드는게 O(N)이기에 문제 조건에 부합X
        # st=0
        # en=len(new)-1
        # while st<=en:
        #     mid = (st+en)//2
        #     if new[mid] == target:
        #         return (mid+pivot)%len(new)
        #     elif new[mid] > target:
        #         en = mid-1
        #     else:
        #         st = mid+1
        # return -1

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
                return st
        




s=Solution()
print(s.search(nums = [3,1], target = 3))
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
print(s.search(nums = [4,5,6,7,0,1,2], target = 3))
print(s.search(nums = [1], target = 0))
print(s.search(nums = [1,3], target = 0))
