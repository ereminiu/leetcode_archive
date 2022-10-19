class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        p, a = [], []

        for i in range(m):
            p.append((i, 0))
            a.append((i, n-1))
        for j in range(n):
            p.append((0, j))
            a.append((m-1, j))
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(x, y, u):
            u.add((x, y))
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < m and 0 <= ny < n and heights[x][y] <= heights[nx][ny] and (nx, ny) not in u:
                    dfs(nx, ny, u)
        
        vp, va = set(), set()
        for x, y in p: 
            dfs(x, y, vp)
        for x, y in a:
            dfs(x, y, va)
        return vp&va