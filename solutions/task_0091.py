class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s == '0' else 1
        
        s = '0'+s
        n = len(s)
        dp = n * [0]
        dp[0] = 1
        
        def get(c):
            return ord(c)-ord('0')

        for i in range(n):
            a, b = get(s[i-1]) * 10 + get(s[i]), get(s[i])
            if b != 0: dp[i] += dp[i-1]
            if b < a <= 26: dp[i] += dp[i-2]
        return dp[n-1]