class Solution {
public:
#define len(a) (int)(a).size()
    bool increasingTriplet(vector<int>& nums) {
        int n = len(nums);
        if (n < 3) {
            return false;
        }
        vector<int> pr(n), sf(n);
        pr[0] = nums[0];
        for (int i = 1; i < n; i++) {
            pr[i] = min(pr[i-1], nums[i]);
        }
        sf[n-1] = nums[n-1];
        for (int i = n-2; i >= 0; i--) {
            sf[i] = max(sf[i+1], nums[i]);
        }
        for (int i = 1; i < n-1; i++) {
            if (pr[i-1] < nums[i] and nums[i] < sf[i+1]) {
                return true;
            }
        }
        return false;
    }
};