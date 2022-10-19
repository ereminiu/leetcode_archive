import bisect

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        cols = list(map(lambda i: matrix[i][0], range(n)))
        col = bisect.bisect_left(cols, target)
        if matrix[n-1][m-1] < target:
            return False
        if col != n and matrix[col][0] == target:
            return True
        col -= 1
        idx = bisect.bisect_left(matrix[col], target)
        return idx != m and matrix[col][idx] == target