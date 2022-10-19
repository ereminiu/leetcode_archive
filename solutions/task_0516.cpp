class Solution {
public:
#define len(a) (int)(a).size()
    int longestPalindromeSubseq(string s) {
        int n = len(s);
        vector<vector<int>> dp(n, vector<int>(n));
        for (int r = 0; r < n; r++) {
            for (int l = r; l >= 0; l--) {
                if (l == r) {
                    dp[l][r] = 1;
                    continue;
                }
                if (l == r-1) {
                    dp[l][r] = (s[l] == s[r] ? 2 : 1);
                } else {
                    if (s[l] == s[r]) {
                        dp[l][r] = max(dp[l][r], dp[l+1][r-1]+2);
                    }
                    dp[l][r] = max({dp[l][r], dp[l+1][r], dp[l][r-1]});
                }
            }
        }
        return dp[0][n-1];
    }
};