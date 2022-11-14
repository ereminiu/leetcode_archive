class Solution:
    def longestPath(self, parent, s: str) -> int:
        n = len(s)
        gr = [[] for i in range(n)]
        root = -1
        for i in range(n):
            if parent[i] != -1:
                gr[i].append(parent[i])
                gr[parent[i]].append(i)
            else:
                root = i
        
        dp = n * [0]
        ans = 0
        def dfs(u, prev):
            dp[u] = 1
            actual = []
            for v in gr[u]:
                if not dp[v]:
                    dfs(v, u)
                if v != prev and s[v] != s[u]:
                    dp[u] = max(dp[u], dp[v]+1)
                    actual.append(dp[v])
            actual.sort(reverse=True)
            nonlocal ans
            if len(actual) > 1:
                ans = max(ans, actual[0]+actual[1]+1)
            else:
                ans = max(ans, dp[u])
            
        dfs(root, -1)
        
        return ans