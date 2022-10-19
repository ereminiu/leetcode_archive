class Solution:
    def totalNQueens(self, n: int) -> int:
        
        maind = set()
        subd = set()
        used_cols = n * [False]
        ans = 0

        def go(row):
            if row == n:
                nonlocal ans
                ans += 1
                return
            for col in range(n):
                main, sub = row-col, -row-col
                if not used_cols[col] and not main in maind and not sub in subd:
                    used_cols[col] = True 
                    maind.add(main); subd.add(sub)
                    go(row+1)
                    used_cols[col] = False
                    maind.remove(main); subd.remove(sub)

        for i in range(n):
            used_cols[i] = True
            maind.add(-i)
            subd.add(-i)
            go(1)
            used_cols[i] = False
            maind.remove(-i)
            subd.remove(-i)
        
        return ans