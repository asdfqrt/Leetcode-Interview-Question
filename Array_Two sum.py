class Solution:
    def twoSum(self, nums, target: int):
        C={}    #딕셔너리가 탐색속도가 훨씬 빠름
        for i in range(len(nums)):  
            if nums[i] in C:    
                return([C[nums[i]],i])  #target-nums값과 위치 저장해둔다 ex) [2,7,11,15],9 의 경우 C={7:0,2:1,-2,2,-6,3}
            else:
                C[target-nums[i]] = i

#nums를 돌며 딕셔너리 확인 및 삽임, O(N) x O(1) = 총 O(N), 이중 for문 O(N^2)보다 빠름

# s = Solution()
# print(s.twoSum([2,7,11,15],9))
# print(s.twoSum([3,2,4],6))
# print(s.twoSum([3,3],6))