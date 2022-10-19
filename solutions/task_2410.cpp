class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        multiset<int> ms;
        for (int e : trainers) {
            ms.insert(e);
        }
        int ans = 0;
        sort(players.begin(), players.end());
        for (int x : players) {
            auto it = ms.lower_bound(x);
            if (it != ms.end()) {
                ms.erase(it);
                ans += 1;
            }
        }
        return ans;
    }
};