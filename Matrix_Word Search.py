#https://leetcode.com/problems/word-search/
#Follow up: Could you use search pruning to make your solution faster with a larger board?
# ba + na 에서 막혀도  bana + na 로 재탐색될수 있어야됨, vis 체크하는걸 좀더 늦춰서? vis체크를 풀면서?
# 통과는 됬는데 시간 굉장히 많이 걸림 >> 처음부터 안될만한 걸 잘라내야됨

class Solution:
    def exist(self, board, word: str) -> bool:
        
        self.m = len(board)
        self.n = len(board[0])
        self.nx = [1,0,-1,0]
        self.ny = [0,1,0,-1]
        self.word = word
        self.lenword = len(word)
        self.board = board
        self.vis = [[False] *self.n for _ in range(self.m)]
        for x in range(self.m):
            for y in range(self.n):
                if board[x][y] == word[0]:
                    if self.dfs(x,y,1): return True
        return False
    
    def dfs(self,x,y,deep):
        if self.lenword == deep: return True
        self.vis[x][y] = True
        letter = self.word[deep]
        for dir in range(4):
            dx = x + self.nx[dir]
            dy = y + self.ny[dir]
            if 0<=dx<self.m and 0<=dy<self.n and not self.vis[dx][dy] and self.board[dx][dy] == letter:
                if self.dfs(dx,dy,deep+1): return True
        self.vis[x][y] = False

s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(s.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
###############################
# 선행조건으로 많이 잘라내기
# any와 chain(*list), counter, product사용은 참고할만할지도

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        if len(word) > m * n: return False                            # [a] trivial case to discard

        if not (cnt := Counter(word)) <= Counter(chain(*board)):      # [b] there are not enough
            return False                                              #     letters on the board
        
        if cnt[word[0]] > cnt[word[-1]]:                              # [c] inverse word if it's better
             word = word[::-1]                                        #     to start from the end
        
        def dfs(i, j, s):                                             # recursive postfix search
            
            if s == len(word) : return True                           # [1] found the word
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:  # [2] found a letter
                board[i][j] = "#"                                     # [3] mark as visited
                adj = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]               # [4] iterate over adjacent cells...
                dp = any(dfs(ii,jj,s+1) for ii,jj in adj)             # [5] ...and try next letter
                board[i][j] = word[s]                                 # [6] remove mark
                return dp                                             # [7] return search result

            return False                                              # [8] this DFS branch failed
                
        return any(dfs(i,j,0) for i,j in product(range(m),range(n)))  # search starting from each position