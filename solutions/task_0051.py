class Solution:
    def solveNQueens(self, n: int) -> int:
        
        maind = set()
        subd = set()
        used_cols = n * [False]
        field = [['.' for x in range(n)] for y in range(n)]
        ans = []

        def go(row):
            if row == n:
                cur = []
                for i in range(n):
                    me = ''
                    for c in field[i]:
                        me += c
                    cur.append(me)
                ans.append(cur)
                return
            for col in range(n):
                main, sub = row-col, -row-col
                if not used_cols[col] and not main in maind and not sub in subd:
                    used_cols[col] = True 
                    maind.add(main); subd.add(sub)
                    field[row][col] = 'Q'
                    go(row+1)
                    field[row][col] = '.'
                    used_cols[col] = False
                    maind.remove(main); subd.remove(sub)

        for i in range(n):
            used_cols[i] = True
            maind.add(-i); subd.add(-i)
            field[0][i] = 'Q'
            go(1)
            field[0][i] = '.'
            used_cols[i] = False
            maind.remove(-i); subd.remove(-i)
        
        return ans