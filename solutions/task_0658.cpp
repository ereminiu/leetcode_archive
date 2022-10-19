class Solution {
public:

    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int delta = x;
        sort(arr.begin(), arr.end(), [&](int a, int b){
            return abs(a-delta) < abs(b-delta) or (abs(a-delta) == abs(b-delta) and a < b);
        });
        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(arr[i]);
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};