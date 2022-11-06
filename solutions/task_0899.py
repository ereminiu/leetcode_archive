class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            sl = list(s)
            sl.sort()
            return ''.join(sl)
        
        ans = s[::]
        for i in range(len(s)):
            ans = min(ans, s[i:]+s[:i])
        return ''.join(ans)

print(Solution().orderlyQueue(s = "cba", k = 2))