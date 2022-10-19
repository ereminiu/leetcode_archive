class DSU:
    def __init__(self, n):
        self.par = n * [0]
        self.size = n * [1]
        for i in range(n):
            self.par[i] = i
    
    def get_par(self, u):
        if self.par[u] == u:
            return u
        pr = self.get_par(self.par[u])
        self.par[u] = pr
        return pr
    
    def unite(self, u, v):
        u, v = self.get_par(u), self.get_par(v)
        if u == v:
            return
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.size[u] += self.size[v]
        self.par[v] = u
    
    def same(self, u, v):
        return self.get_par(u) == self.get_par(v)


class Solution:
    def equationsPossible(self, equations) -> bool:
        
        def get(c):
            return ord(c)-ord('a')
        
        ufo = DSU(26)
        q = []
        for s in equations:
            a, b = get(s[0]), get(s[-1])
            if s[1]+s[2] == '==':
                ufo.unite(a, b)
            else:
                q.append([a, b])
        for a, b in q:
            if ufo.same(a, b):
                return False
        return True

# print(Solution().equationsPossible(["a==b","b!=c","c==a"]))