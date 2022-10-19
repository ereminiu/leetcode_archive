class Solution:
    def get_sum(self, x1, y1, x2, y2):
        result = self.pref[x2][y2]
        if x1 > 0: result -= self.pref[x1-1][y2]
        if y1 > 0: result -= self.pref[x2][y1-1]
        if x1 > 0 and y1 > 0: result += self.pref[x1-1][y1-1]
        return result
    
    def largest1BorderedSquare(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        self.pref = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m):
                self.pref[i][j] = grid[i][j]
                if i > 0: self.pref[i][j] += self.pref[i-1][j]
                if j > 0: self.pref[i][j] += self.pref[i][j-1]
                if i > 0 and j > 0: self.pref[i][j] -= self.pref[i-1][j-1]
        ans = 0
        for i in range(n):
            for j in range(m):
                for k in range(min(n-i, m-j)):
                    if self.get_sum(i, j, i+k, j) == k+1 and self.get_sum(i, j, i, j+k) == k+1 and \
                       self.get_sum(i+k, j, i+k, j+k) == k+1 and self.get_sum(i, j+k, i+k, j+k) == k+1:
                       ans = max(ans, (k+1)**2)
        return ans