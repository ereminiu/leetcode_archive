class MagicDictionary:

    def __init__(self):
        self.st = set()
        self.mod = int(1e9+7)

    def count_hash(self, s):
        base = 37
        n = len(s)
        res = 0
        for c in s:
            res = (res * base + ord(c)-ord('a')+1) % self.mod
        return res
        
    def buildDict(self, dictionary) -> None:
        base = 37
        
        maxlen = 0
        for s in dictionary:
            self.st.add(self.count_hash(s))
            maxlen = max(maxlen, len(s))
        self.deg = (maxlen+1) * [0]
        self.deg[0] = 1
        for i in range(1, maxlen+1):
            self.deg[i] = (self.deg[i-1] * base) % self.mod

    def search(self, searchWord: str) -> bool:
        
        def get(c):
            return ord(c)-ord('a')+1
        
        n = len(searchWord)
        myhash = self.count_hash(searchWord)
        if n > len(self.deg)-1:
            return False
        for i in range(n):
            for c in range(1, 27):
                if get(searchWord[i]) == c:
                    continue
                new_hash = (myhash - (get(searchWord[i]) - c) * self.deg[n-i-1] + self.mod) % self.mod
                if new_hash in self.st:
                    return True
        return False