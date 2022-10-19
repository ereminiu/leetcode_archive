class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        dp = (amount+1) * [int(1e9+228)]
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0 and dp[i-c] + 1 < dp[i]:
                    dp[i] = dp[i-c] + 1
        return -1 if dp[amount] == int(1e9+228) else dp[amount]