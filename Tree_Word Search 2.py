# https://leetcode.com/problems/word-search/
# 각 word마다 매번 새로 초기화된 board에서 찾는방법은 O(N) * O(m*n)(스타트지점 변경) * O(m*n) (floodfill)
# 그것보다 trie 구조로 word를 받아두고 하는건 어떰?
# 매 칸에서 시작하는 word 있나 탐색하는것
# 실제 코드 실행해보니 다른사람들 코드보다 많이 느림, 트라이에서 단어 한개 찾고나면 만약 그단어가 더이상 없으면 그 route에 있던 노드들 다 지워야 되는듯
# 지우는과정에서 parent 있으면 편함
class Node:
    def __init__(self):
        self.parent = None  # 기존 trie에는 필요없지만 삭제시 있으면 편함
        self.child = {}
        self.end = False

    def addWords(self,words):
        for word in words:
            cur = self
            for string in word:
                if string not in cur.child:
                    cur.child[string] = Node()
                    cur.child[string].parent = cur
                cur = cur.child[string]
            cur.end = True
    def delWord(self,cur,route):    # 여기서 시간 줄임
        idx = len(route)
        while not cur.child and cur.parent: # 자식노드가 없는경우(route에 있는 단어가 나뿐인) 노드를 지워가며 자식노드가 있는 곳 or 루트노드까지 감
            idx-=1
            cur = cur.parent
            del cur.child[route[idx]] #prev노드가 들어간 키값을 줘야됨

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(x,y,cur,route):
            if cur.end:
                ans.add(route)
                root.delWord(cur,route)
            if len(route) == maxlen: return False
            vis[x][y] = True
            for dir in range(4):
                dx = x + nx[dir]
                dy = y + ny[dir]
                if 0<=dx<m and 0<=dy<n and not vis[dx][dy] and board[dx][dy] in cur.child:
                    dfs(dx,dy,cur.child[board[dx][dy]],route+board[dx][dy])
            vis[x][y] = False

        root = Node()
        root.addWords(words)
        m = len(board)
        n = len(board[0])
        maxlen = 0
        for word in words:
            if len(word) > maxlen: maxlen = len(word)
        nx = [1,0,-1,0]
        ny = [0,1,0,-1]
        vis = [[False]*n for _ in range(m)]
        ans = set()


        for x in range(m):
            for y in range(n):
                if board[x][y] in root.child:
                    dfs(x,y,root.child[board[x][y]],board[x][y])
        
        return ans
        
        
