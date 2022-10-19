class Solution {
public:
#define len(a) (int)(a).size()
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        vector<pair<int, int>> toSort(n);
        for (int i = 0; i < n; i++) {
            toSort[i] = {-efficiency[i], speed[i]};
        }
        sort(toSort.begin(), toSort.end());
        for (int i = 0; i < n; i++) {
            efficiency[i] = -toSort[i].first;
            speed[i] = toSort[i].second;
            // cerr << speed[i] << ' ' << efficiency[i] << endl;
        }
        multiset<long long> st;
        long long sum = 0;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(ans, (sum + speed[i]) * efficiency[i]);
            if (len(st) < k-1) {
                sum += speed[i];
                st.insert(speed[i]);
                continue;
            }
            if (len(st) > 0 and speed[i] > *st.begin()) {
                sum -= *st.begin();
                st.erase(st.begin());
                st.insert(speed[i]);
                sum += speed[i];
            }
        }
        const int MOD = 1e9 + 7;
        return ans % MOD;
    }
};
