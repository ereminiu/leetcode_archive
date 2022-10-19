class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = int(arr.size());
        vector<vector<int>> dp(n, vector<int>(n, 2));
        int ans = 0;
        for (int j = n-2; j >= 1; j--) {
            int k = j+1;
            for (int i = 0; i < j; i++) {
                while (k < n and arr[i]+arr[j] > arr[k]) {
                    k += 1;
                }
                if (k < n and arr[i] + arr[j] == arr[k]) {
                    dp[i][j] = dp[j][k]+1;
                    ans = max(ans, dp[i][j]);
                }
            }
        }
        return ans;
    }
};