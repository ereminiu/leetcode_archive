class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        pref = n * [0]
        pref[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            pref[i] = max(prices[i], pref[i+1])
        ans = 0
        for i in range(n-1):
            ans = max(ans, pref[i+1]-prices[i])
        return ans