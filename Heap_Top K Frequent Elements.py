# https://leetcode.com/problems/top-k-frequent-elements/
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# counter로 센다음 정렬하고 앞에 몇개 가져오면될듯. 최악의 경우에도 nlogn이고 하나라도 2개이상 나오면 더 적어짐

from collections import Counter
class Solution:
    def topKFrequent(self, nums, k: int):
        array = Counter(nums).most_common()
        ans = []
        for i in range(k):
            ans.append(array[i][0])
        return ans


s = Solution()
print(s.topKFrequent([1],1))