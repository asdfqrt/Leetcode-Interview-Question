#정렬되어있다는 말이 x
# 이전꺼랑 비교하기하려면 sort해줘야될듯
class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = []
        for i,interval in enumerate(intervals):
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1] = [ans[-1][0],max(ans[-1][1],interval[1])]
        return ans
