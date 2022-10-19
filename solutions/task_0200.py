class Solution:
    def inside(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m
    
    def dfs(self, i, j, color):
        self.comp[i][j] = color
        for k in range(4):
            ni, nj = i+self.dx[k], j+self.dy[k]
            if self.inside(ni, nj) and self.grid[ni][nj] == "1" and self.comp[ni][nj] == 0:
                self.dfs(ni, nj, color)

    def numIslands(self, grid) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.comp = [[0 for x in range(self.m)] for y in range(self.n)]
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, -1, 1]
        color = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == "1" and self.comp[i][j] == 0:
                    color += 1
                    self.dfs(i, j, color)
        # print(*self.comp, sep='\n')
        return color