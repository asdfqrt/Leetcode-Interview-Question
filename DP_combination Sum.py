# #Follow up: What if negative numbers are allowed in the given array?
# # How does it change the problem?
# # What limitation we need to add to the question to allow negative numbers?
# # 음수가 들어갈수 있으면 [-1, 1] 넣고 1만들라는 조합에서 [1],[-1,1,1],[-1,1,-1,1,1] 처럼 함쳐 0맏늘어서 무한대 가능


# #아마 재귀로 풀수있을거 같은데
# #재귀로 하고 시간초과나면 memoization이나 dp고려해보면될듯
# output = 0
# class Solution:
#     def combinationSum4(self, nums, target: int) -> int:
#         global output
#         self.solve(nums,target)
#         return output

    
#     def solve(self, nums,target):
#         global output
#         for i in nums:
#             if i == target: output += 1
#             elif i< target: self.solve(nums,target-i)

# s = Solution()
# print(s.combinationSum4(nums = [9], target = 3))
# print(s.combinationSum4(nums = [1,2,3], target = 4))

#내 컴에서는 돌아가는데 leetcode에서는 다른 결과나옴 >> global변수 쓰면 이게 다음 테스트 케이스에도 적용되기 때문이라함
# 걍 dp로 푸는게 나을듯
# d[x] = 수 x를 만드는 가짓수, d[x+nums안 숫자] += d[x]
# d[target] 하면될듯

class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        d = [0] * 1001
        for i in nums: d[i] = 1
        for i in range(target):
            for j in nums:
                if i+j <= target: d[i+j] += d[i]
        return d[target]
s = Solution()
print(s.combinationSum4(nums = [1,2,3], target = 4))
print(s.combinationSum4(nums = [9], target = 3))