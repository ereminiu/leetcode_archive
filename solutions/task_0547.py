class Solution:
    def dfs(self, u):
        self.used[u] = True
        for v in range(self.n):
            if self.gr[u][v] and not self.used[v]:
                self.dfs(v)
    
    def findCircleNum(self, isConnected) -> int:
        self.gr = isConnected
        self.n = len(isConnected)
        self.used = self.n * [False]
        count = 0
        for i in range(self.n):
            if not self.used[i]:
                count += 1
                self.dfs(i)
        return count