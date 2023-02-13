#이분탐색하면 될듯?
#start순으로 정렬되있따 하지만 겹치지 않는다 했으면  end로도 정렬될수밖에 없음
from bisect import bisect_left
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        if intervals[0][0] > newInterval[1]: return [newInterval]+intervals
        if intervals[-1][1] < newInterval[0]: return intervals+[newInterval]

        n = len(intervals)
        st = bisect_left(intervals,newInterval)
        en = bisect_left(intervals,[newInterval[1]])
        st -=1 if  (st!=0 and intervals[st-1][1] >= newInterval[0]) else 0
        en -=1 if en==n or (en!=0 and intervals[en][0] > newInterval[1]) else 0
        
        if st>en:
            return intervals[:st] + [newInterval] + intervals[st:]

        intervals[st].extend(newInterval)
        intervals[st].extend(intervals[en])
        if en != n-1:
            return intervals[:st] +[[min(intervals[st]),max(intervals[st])]] + intervals[en+1:]
        else:
            return intervals[:st] +[[min(intervals[st]),max(intervals[st])]]


s = Solution()
s.insert([[3,5],[12,15]],newInterval =[6,8])
s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])


#########################
#이쪽이 나은듯
class Solution:
    def insert(self, intervals, newInterval):
        # O(logN)
        position = bisect.bisect(intervals, newInterval)
        # O(N)
        intervals.insert(position, newInterval)

        answer = []
        # O(N)
        for i in range(len(intervals)):
            if not answer or intervals[i][0] > answer[-1][1]:
                answer.append(intervals[i])
            else:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])

        return answer