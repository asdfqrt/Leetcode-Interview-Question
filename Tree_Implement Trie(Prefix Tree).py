# https://leetcode.com/problems/implement-trie-prefix-tree/
class Node:
    def __init__(self,x):
        self.val = x
        self.last = False
        self.adj = []

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        cur = self.root
        for string in word:
            exist = False
            for dir in cur.adj:
                if dir.val==string:
                    cur=dir
                    exist = True
                    break
            if not exist:
                cur.adj.append(Node(string))
                cur = cur.adj[-1]
        cur.last = True
                

    def search(self, word: str) -> bool:
        cur = self.root
        for string in word:
            exist = False
            for dir in cur.adj:
                if dir.val==string:
                    cur=dir
                    exist = True
                    break
            if not exist:
                return False
        return cur.last

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for string in prefix:
            exist = False
            for dir in cur.adj:
                if dir.val==string:
                    cur=dir
                    exist = True
                    break
            if not exist:
                return False
        return True
            

obj = Trie()
obj.insert("apple")
obj.insert("apart")
print(obj.startsWith("app"))
print(obj.startsWith("apd"))
print(obj.search("appl"))
print(obj.search("apart"))
###############################
#다른사람 코드 dict활용해서 코드 간결화
class TNode:
    def __init__(self):
        self.child={}
        self.isWordFinished=False

class Trie:
    def __init__(self):
        self.root=TNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i not in cur.child:
                cur.child[i]=TNode()
            cur=cur.child[i]
        cur.isWordFinished=True

    def search(self, word: str) -> bool:
        cur=self.root
        for i in word:
            if i not in cur.child:
                return False
            cur=cur.child[i]
        return cur.isWordFinished     

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for i in prefix:
            if i not in cur.child:
                return False
            cur=cur.child[i]
        return True