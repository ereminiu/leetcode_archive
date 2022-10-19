class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int n = int(nums1.size()), m = int(nums2.size());
        vector<vector<int>> dp(n, vector<int>(m));
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (nums1[i] == nums2[j]) {
                    dp[i][j] = 1;
                    if (i > 0 and j > 0) {
                        dp[i][j] += dp[i-1][j-1];
                    }
                }
                ans = max(ans, dp[i][j]);
            }
        }
        return ans;
    }
};
