class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = n * [0]
        ans = 0
        for i in range(1, n):
            if s[i-1]+s[i] == '()':
                dp[i] = (0 if i < 2 else dp[i-2]) + 2
            elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] + s[i] == '()':
                dp[i] = (0 if i-dp[i-1]-2 < 0 else dp[i-dp[i-1]-2]) + dp[i-1] + 2
            ans = max(ans, dp[i])
        
        return ans