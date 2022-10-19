class Solution {
public:
#define len(a) (int)(a).size()
    int maxProfit(int k, vector<int>& prices) {
        int n = len(prices);
        if (n == 0) {
            return 0;
        }
        vector<vector<int>> dp(k+1, vector<int>(n+11));
        for (int i = 1; i <= k; i++) {
            int prevMax = -int(1e9+228);
            for (int j = 1; j < n; j++) {
                int profit = dp[i-1][j-1] - prices[j-1];
                prevMax = max(prevMax, profit);
                dp[i][j] = max(dp[i][j-1], prevMax+prices[j]);
            }
        }
        return dp[k][n-1];
    }
};