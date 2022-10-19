class Solution {
public:
    vector<vector<int>> pref;
    int n, m;
    
    int get_sum(int i1, int j1, int i2, int j2) {
        int ret = pref[i2][j2];
        if (i1 > 0) {
            ret -= pref[i1-1][j2];
        }
        if (j1 > 0) {
            ret -= pref[i2][j1-1];
        }
        if (i1 > 0 and j1 > 0) {
            ret += pref[i1-1][j1-1];
        }
        return ret;
    }
    
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        // cout << endl;
        n = int(matrix.size()), m = int(matrix[0].size());
        pref.resize(n, vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                pref[i][j] = matrix[i][j];
                if (i > 0) {
                    pref[i][j] += pref[i-1][j];
                }
                if (j > 0) {
                    pref[i][j] += pref[i][j-1];
                }
                if (i > 0 and j > 0) {
                    pref[i][j] -= pref[i-1][j-1];
                }
            }
        }
        int ans = -int(1e9+228);
        for (int row1 = 0; row1 < n; row1++) {
            for (int row2 = row1; row2 < n; row2++) {
                set<int> st;
                for (int i = 0; i < m; i++) {
                    int sum = get_sum(row1, 0, row2, i);
                    auto it = st.lower_bound(sum-k);
                    if (it != st.end()) {
                        ans = max(ans, sum-*it);
                        // cout << "it = " << *it << endl;
                    }
                    if (sum <= k) {
                        ans = max(ans, sum);
                    }
                    st.insert(sum);
                    // cout << sum << endl;
                }
            }
        }
        return ans;
    }
};