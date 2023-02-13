#LIS 문제
#그냥 기억해내서 풀면될듯
#d[x] = x를 마지막으로 하는 증가 부분수열의 길이
# O(N^2) 계산식은 떠오르는데 O(NlogN)으로 풀어보라함 > 아마 이분탐색으로 +1할 숫자를 바로 찾아버리면 될거 같긴한데
# 이분탐색은 정렬이 되어있어야 가능, 매 새로운 d[x]를 확인할때 마다 앞에 있던 것들을 정렬하는방법?
# # 정렬이 nlogn이니까 정렬하고 바로 값을 알수있어도 n^2logn
# heapq 만들어서 문자열 길이 최대 힙으로 pop하는 방법? > pop, push는  logN인데  1000,999,998,997,...,2,1 같은경우 1에서만 nlogn인거같기도
# 처음부터 d 행렬자체를 LIS가 아닌 이분탐색을 위해 정렬된 방식으로 만들어버리면 될듯 어짜피 max값만 뽑는거니까

# class Solution:
#     def lengthOfLIS(self, nums) -> int:
#         d =[]
#         for i in range(len(nums)):
#             d.append(1)
#             for j in range(i):
#                 if nums[i] > nums[j]: d[i] = max(d[j]+1,d[i])
#         return max(d)


# s=Solution()
# print(s.lengthOfLIS(nums = [7,7,7,7,7,7,7]))


import bisect
class Solution:
    def lengthOfLIS(self, nums) -> int:
        d = [nums[0]]
        for i in nums:
            if d[-1] < i: d.append(i)
            else: d[bisect.bisect_left(d,i)] = i
        return len(d)
#실제로는 LIS를 만족하지 않는 상태 ex) 10,20,30,15 주어졌을경우 d = [10,15,30] 됨
#d의 기존 값을 더 작은 값으로 대치하여 이후 원소가 더 많이 들어 올 수 있는 가능성을 넓히는 과정
#어디까지나 '길이'를 구하는데 한정하여 이분탐색을 활용해 풀이 할 수 있다


s=Solution()
print(s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
