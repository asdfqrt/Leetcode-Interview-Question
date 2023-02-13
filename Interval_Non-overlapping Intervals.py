# 그리디인듯?
# 시작점 빠른순으로 정렬하고 겹치면 end가 짧은거를 남기면 될듯
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        ans = []
        cnt = 0
        for interval in intervals:
            if not ans or ans[-1][1] <= interval[0]:
                ans.append(interval)
            elif interval[1] <= ans[-1][1]:
                ans[-1] = interval
                cnt +=1
            else: cnt +=1
        return cnt




s = Solution()
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))


######################
# end를 기준으로 정렬하는쪽이 좀더 직관적
# 빨리끝나는걸 먼저 잡기
def eraseOverlapIntervals(intervals):
	end, cnt = float('-inf'), 0
	for s, e in sorted(intervals, key=lambda x: x[1]):
		if s >= end: 
			end = e
		else: 
			cnt += 1
	return cnt
