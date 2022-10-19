class myTrie:
    class Node:
        def __init__(self):
            self.next = 26 * [None]
            self.fl = False
    
    def __init__(self):
        self.root = self.Node()
        self.beg = chr(ord('z')+1)

    def get(self, c):
        return ord(c)-ord('a')

    def __add(self, u, s, k):
        if k == len(s)-1:
            u.fl = True
            return
        idx = self.get(s[k+1])
        if not u.next[idx]:
            u.next[idx] = self.Node()
        self.__add(u.next[idx], s, k+1)

    def __find(self, u, s, k):
        if k == len(s)-1:
            return u.fl
        idx = self.get(s[k+1])
        if not u.next[idx]:
            return False
        return self.__find(u.next[idx], s, k+1)

    def __erase(self, u, s, k):
        if k == len(s)-1:
            u.fl = False
            return 
        idx = self.get(s[k+1])
        if not u.next[idx]:
            return
        self.__erase(u.next[idx], s, k+1)

    def __ispref(self, u, s, k):
        if k == len(s)-1:
            return (u != None)
        idx = self.get(s[k+1])
        if not u.next[idx]:
            return False
        return self.__ispref(u.next[idx], s, k+1)
    
    def ispref(self, s):
        return self.__ispref(self.root, self.beg + s, 0)
    
    def erase(self, s):
        return self.__erase(self.root, self.beg + s, 0)
    
    def find(self, s):
        return self.__find(self.root, self.beg + s, 0)
    
    def add(self, s):
        return self.__add(self.root, self.beg + s, 0)

class Trie:

    def __init__(self):
        self.trie = myTrie()

    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.find(word)

    def startsWith(self, prefix: str) -> bool:
        return self.trie.ispref(prefix)
