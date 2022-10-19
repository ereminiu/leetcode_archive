class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b) {
        if (a[0] != b[0])
            return a[0] > b[0];
        return a[1] < b[1];
    }

    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        sort(properties.begin(), properties.end(), cmp);
        int curmax = -int(1e9);
        int ans = 0;
        for (auto p : properties) {
            if (curmax > p[1]) {
                ans += 1;
            }
            curmax = max(curmax, p[1]);
        }
        return ans;
    }
};