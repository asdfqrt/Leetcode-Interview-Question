# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# 깊이,left or right,현재노드 나오면될듯?
# 다시만드는 그래프는 스택으로 불러오면될듯?
from collections import deque
class Codec:

    def serialize(self, root):
        if not root: return ""
        code = ""
        def dfs(cur,dep):
            nonlocal code
            code += str(cur.val) + ","
            if cur.left:
                code += str(dep+1)
                code += "l"
                dfs(cur.left,dep+1)
            if cur.right:
                code += str(dep+1)
                code +="r"
                dfs(cur.right,dep+1)
        dfs(root,0)
        return code
        

    def deserialize(self, data):
        if not data: return None
        q = deque([])
        for n,string in enumerate(data.split(",")):
            if n==0:
                root = TreeNode(string)
                cur_dep,cur = 0,root
                q.append((cur_dep,cur))
            elif string:
                if "l" in string:
                    dir_dep,childval =  map(int,string.split("l"))
                    child = TreeNode(childval)
                    # while dir_dep <= cur_dep:
                    #     cur_dep,cur = q.pop()        #left에서는 이 부분 필요없는듯            
                    cur.left = child
                else:
                    dir_dep,childval =  map(int,string.split("r"))
                    child = TreeNode(childval)
                    while dir_dep <= cur_dep:
                        cur_dep,cur = q.pop()                  
                    cur.right = child
                cur_dep,cur = dir_dep,child
                q.append((cur_dep,cur))
        return root



#########################
# 다른사람풀이
# dfs의 탐색순서는 항상 동일하니 dfs로 탐색해서 빈칸은 #으로 하고 이후 탐색을 더 하지 않는 방식으로 코드작성
# 12##345는 [1,2,3,null,null,4,5] 뜻하는것
# 이후 재현에서 #만나면 null 반환, 아니면 그값의 노드 반환하면서 더 탐색

class Codec:

    def serialize(self, root):
        def dfs(cur):
            if cur:
                vals.append(str(cur.val))
                dfs(cur.left)
                dfs(cur.right)
            else:
                vals.append('#')
        vals = []
        dfs(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def dfs():
            cur_val = next(vals)
            if cur_val == "#":
                return None
            cur = TreeNode(int(cur_val))
            cur.left = dfs()
            cur.right = dfs()
            return cur()
        
        vals = iter(data.split())
        return dfs()