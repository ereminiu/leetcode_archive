class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # @cache
        def solve(i, c, cnt, k):
            if k < 0:
                return int(1e9+228)
            if i == len(s):
                return 0
            delete, keep = solve(i+1, c, cnt, k-1), 0
            if s[i] == c:
                keep = solve(i+1, c, cnt+1, k)
                if cnt in [1, 9, 99, 999]:
                    keep += 1
            else:
                keep = solve(i+1, s[i], 1, k) + 1
            return min(delete, keep)
        
        return solve(0, '', 0, k)