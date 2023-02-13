# https://leetcode.com/problems/find-median-from-data-stream/
# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# 1~100이면 one hot 인코딩 쓰면 더 빠르게 가능

# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# 메디안은 평균이 아니라 중간값
# 중간값 없을 경우에만 두 중간값 근처 값의 평균
# 시간초과남. 데이터 구조 자체에서 O(1)에 가깝게 median을 뽑을수 있어야되나봄

import statistics as st
class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        return (st.median_low(self.array)+st.median_high(self.array))/2


################
# O(1)에 찾으려면 c++의 ordered multiset 같은게 필요한데 없는데로 중간까지 다뺴기
# TLE
from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        self.q = []
        self.len = 0

    def addNum(self, num: int) -> None:
        heappush(self.q,num)
        self.len += 1

    def findMedian(self) -> float:
        if self.len==0:
            return None
        temp = []
        while len(self.q)!=(self.len//2):
            temp.append(heappop(self.q))
        res = (temp[-1]+self.q[0])/2 if self.len%2==0 else temp[-1]
        for i in temp:
            heappush(self.q,i)
        return res



#####################
# 현 중간값보다 큰값 작은값을 각각 min,max힙에 넣고 관리
# 삽입에 최대 O(3logn), 탐색에 O(2)
from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            heappush(self.minheap,num)
            self.b =1
        elif num > self.minheap[0]:
            heappush(self.minheap,num)
            self.b +=1
            if self.b >1:
                heappush(self.maxheap,-heappop(self.minheap))
                self.b -=2
        else:
            heappush(self.maxheap,-num)
            self.b -=1
            if self.b<0:
                heappush(self.minheap,-heappop(self.maxheap))
                self.b +=2

    def findMedian(self) -> float:
        if not self.minheap:
            return None
        if self.b==1:
            return self.minheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2


med = MedianFinder()
med.addNum(6)
print(med.findMedian())
med.addNum(10)
print(med.findMedian())
med.addNum(2)
print(med.findMedian())
