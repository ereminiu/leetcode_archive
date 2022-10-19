class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)

        ans = 0
        prev = 26 * [-1]
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            previdx = prev[idx]
            prev[idx] = i
            ans += (i-previdx) * (n-i)
        return ans