from collections import deque

class Solution:
    def minimumObstacles(self, grid) -> int:
        n, m = len(grid), len(grid[0])

        def inside(x, y):
            return 0 <= x < n and 0 <= y < m

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        inf = int(1e9+228)
        dist = [[inf for x in range(m)] for y in range(n)]
        dq = deque()
        dq.appendleft((0, 0))
        dist[0][0] = 0
        while len(dq):
            u = dq.popleft()
            x, y = u
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if not inside(nx, ny):
                    continue
                w = grid[nx][ny]
                if dist[nx][ny] > dist[x][y] + w:
                    dist[nx][ny] = dist[x][y] + w
                    if w == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

        return dist[n-1][m-1]