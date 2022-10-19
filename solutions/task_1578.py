class Solution:
    def minCost(self, s: str, a) -> int:
        i, j = 0, 0
        n = len(a)
        ans = 0
        while i < n and j < n:
            cur, mx = 0, 0
            while j < n and s[i] == s[j]:
                cur += a[j]
                mx = max(mx, a[j])
                j += 1
            ans += cur-mx
            i = j
        return ans