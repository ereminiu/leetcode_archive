class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix); m = len(matrix[0])
        shift = (n+1) * [0]
        matrix.append([int(1e9+228)])
        a = []
        while True:
            if len(a) >= k:
                break
            idx = n
            for i in range(n):
                if shift[i] < m and matrix[i][shift[i]] < matrix[idx][shift[idx]]:
                    idx = i
            a.append(matrix[idx][shift[idx]])
            shift[idx] += 1
        return a[k-1]