#사이클이 생기면 안되는듯
#조건을 따라 올라가면될듯
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # self.adj =[[] for _ in range(numCourses)]
        self.adj ={i:[] for i in range(numCourses)}   #파이썬의 adj는 dic을 쓰는게 더 좋나봄
        self.ok = set()
    
        for course,prereq in prerequisites:
            self.adj[course].append(prereq)

        for i in range(numCourses):
            if i not in self.ok:
                self.cycle = set()
                if not self.dfs(i): return False
        return True

    def dfs(self, cur):
        self.cycle.add(cur)
        for dir in self.adj[cur]:
            if dir in self.ok: continue
            if dir in self.cycle or not self.dfs(dir): return False
        self.cycle.remove(cur)
        self.ok.add(cur)
        return True
s = Solution()
print(s.canFinish( numCourses = 2, prerequisites = [[1,0]]))
print(s.canFinish( numCourses = 2, prerequisites = [[1,0],[0,1]]))


    



