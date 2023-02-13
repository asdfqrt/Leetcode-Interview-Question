
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node: return node
        self.clone = {}
        self.dfs(node)
        return self.clone[node.val]

    def dfs(self, node):
        self.clone[node.val] = Node(node.val)
        for dir in node.neighbors:
            if dir.val not in self.clone: self.dfs(dir)
            self.clone[node.val].neighbors += [self.clone[dir.val]]


class Solution:
    def cloneGraph(self, node):
        if not node: return node
        self.clone = {}
        self.dfs(node)
        return self.clone[node]

    def dfs(self, node):
        self.clone[node] = Node(node.val)   # 그냥 node 자체를 key로 쓸 수 있다, neighbors은 직접 탐색하고 Node val만 받아와야 복사 안되는듯??
        for dir in node.neighbors:
            if dir not in self.clone: self.dfs(dir)
            self.clone[node].neighbors.append(self.clone[dir])
#dfs

class Solution:
    def cloneGraph(self, node):
        if not node: return node
        q = deque([node])
        clone = {}
        clone[node] = Node(node.val)

        while q:
            cur = q.popleft()
            for dir in cur.neighbors:
                if dir not in clone:
                    clone[dir] = Node(dir.val)
                    q.append(dir)
                clone[cur].neighbors.append(clone[dir])
        return clone[node]

#bfs