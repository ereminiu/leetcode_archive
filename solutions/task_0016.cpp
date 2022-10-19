class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = int(nums.size());
        int ans = 0;
        int closest = int(1e9+228);
        for (int i = 0; i < n-2; i++) {
            int s = i+1, e = n-1;
            while (s < e) {
                int sum = nums[i] + nums[s] + nums[e];
                int df = abs(sum-target);

                if (df < closest) {
                    closest = df;
                    ans = sum;
                }

                if (sum > target) {
                    e -= 1;
                } else {
                    s += 1;
                }
            }
        }
        return ans;
    }
};