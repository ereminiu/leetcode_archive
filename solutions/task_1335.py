class Solution:
    def minDifficulty(self, a, d: int) -> int:
        n = len(a)
        
        # @cache
        def solve(i, k):
            if k == d:
                return max(a[i:])
            ret = int(1e9+228)
            cur = 0
            for j in range(i, n-d+k):
                cur = max(cur, a[j])
                ret = min(ret, cur + solve(j+1, k+1))
            return ret
        
        return -1 if d > n else solve(0, 1)