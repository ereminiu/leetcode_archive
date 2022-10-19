class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int inf = int(1e9+228);
        int ans = inf;
        int n = int(tops.size());
        map<int, int> c;
        for (int i = 0; i < n; i++) {
            int a = tops[i], b = bottoms[i];
            c[a] += 1;
            c[b] += 1;
            if (a == b) {
                c[a] -= 1;
            }
        }
        vector<int> valid;
        for (int i = 0; i < 7; i++) {
            if (c[i] == n) {
                valid.push_back(i);
            }
        }
        for (int v : valid) {
            int top = 0, bot = 0;
            for (int i = 0; i < n; i++) {
                if (tops[i] != v) {
                    if (bottoms[i] == v) {
                        top += 1;
                    } else {
                        top = inf;
                    }
                }
                if (bottoms[i] != v) {
                    if (tops[i] == v) {
                        bot += 1;
                    } else {
                        bot = inf;
                    }
                } 
            }
            ans = min({ans, top, bot});
        }
        if (ans >= inf) return -1;
        return ans;
    }
};