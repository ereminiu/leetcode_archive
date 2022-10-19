from collections import Counter

class Solution:
    def build(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.pref[i][j] = matrix[i][j]
                if i > 0:
                    self.pref[i][j] += self.pref[i-1][j]
                if j > 0:
                    self.pref[i][j] += self.pref[i][j-1]
                if i > 0 and j > 0:
                    self.pref[i][j] -= self.pref[i-1][j-1]
    
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        n = len(matrix); m = len(matrix[0])
        self.pref = [[0 for x in range(m)] for y in range(n)]
        self.build(matrix)
        ans = 0
        for row_a in range(n):
            for row_b in range(row_a, n):
                counter = Counter()
                for i in range(m):
                    sum = self.pref[row_b][i]
                    if row_a > 0:
                        sum -= self.pref[row_a-1][i]
                    ans += counter[sum - target]
                    if sum == target:
                        ans += 1
                    counter[sum] += 1
        return ans