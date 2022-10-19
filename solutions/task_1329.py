from collections import defaultdict
import heapq

class Solution:
    def diagonalSort(self, mat):
        n, m = len(mat), len(mat[0])
        h = defaultdict(list)
        for r in range(n):
            for c in range(m):
                heapq.heappush(h[c-r], mat[r][c])
        for r in range(n):
            for c in range(m):
                mat[r][c] = heapq.heappop(h[c-r])
        return mat