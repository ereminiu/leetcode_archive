from math import log10

class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        ans = set()

        def go(last_digit, path):
            if int(log10(path)) == n-1:
                ans.add(path)
                return
            if last_digit + k < 10:
                go(last_digit + k, path * 10 + last_digit + k)
            if last_digit - k >= 0:
                go(last_digit - k, path * 10 + last_digit - k)
        
        for i in range(1, 10):
            go(i, i)
        
        return list(ans)