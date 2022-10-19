class Solution {
public:
    bool reorderedPowerOf2(int n) {
        set<vector<int>> powersOf2;
        for (int k = 0; k < 31; k++) {
            int me = (1<<k);
            vector<int> d;
            while (me > 0) {
                d.push_back(me%10);
                me /= 10;
            }
            sort(d.begin(), d.end());
            powersOf2.insert(d);
        }
        vector<int> d;
        while (n > 0) {
            d.push_back(n%10);
            n /= 10;
        }
        sort(d.begin(), d.end());
        return powersOf2.count(d);
    }
};