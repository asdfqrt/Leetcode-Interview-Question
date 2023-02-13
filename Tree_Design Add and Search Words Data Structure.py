# https://leetcode.com/problems/design-add-and-search-words-data-structure
# 트라이 만들고 search중 dot나오면 현재 있는 모든 adj에 대해 탐색하면될듯


class Node:
    def __init__(self):
        self.adj = {}
        self.last = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for string in word:
            if string not in cur.adj:
                cur.adj[string] = Node()
            cur = cur.adj[string]
        cur.last = True
        
    def search(self, word: str) -> bool:
        def dfs(cur,pos):
            nonlocal word
            if pos == len(word):
                return cur.last
            string = word[pos]
            if string == ".":
                if any(dfs(cur.adj[dir],pos+1) for dir in cur.adj):
                    return True
                else:
                    return False
            elif string not in cur.adj:
                return False
            return dfs(cur.adj[string],pos+1)
        return dfs(self.root,0)



obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")

# print(obj.search("pad"))
# print(obj.search("bad"))
# print(obj.search(".ad"))
# print(obj.search("b.."))

obj.addWord("a")
obj.addWord("a")

print(obj.search("."))
print(obj.search("aa"))
print(obj.search("a"))
print(obj.search(".a"))
print(obj.search("a."))


#####################
#다른사람 코드
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.max_len = 0
    def addWord(self, word: str) -> None:
        self.max_len = max(len(word), self.max_len)
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True
    def search(self, word: str) -> bool:
        if len(word) > self.max_len:
            return False
        def dfs(index: int, root: TrieNode) -> bool:
            cur = root
            for i in range(index, len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.end
        return dfs(0, self.root)