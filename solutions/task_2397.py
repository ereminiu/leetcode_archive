class Solution:
    def maximumRows(self, mat, cols: int) -> int:
        
        n, m = len(mat), len(mat[0])
        
        def f(row):
            ret = 0
            for i in range(n):
                fl = True
                for j in range(m):
                    if mat[i][j] > row[j]:
                        fl = False
                        break
                if fl:
                    ret += 1
            return ret
        
        ans = 0
        
        for mask in range(0, 2**m):
            row = []
            for i in range(m):
                if mask & 2**i:
                    row.append(1)
                else:
                    row.append(0)
            if row.count(1) <= cols:
                ans = max(ans, f(row))
        
        return ans