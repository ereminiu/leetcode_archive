class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = n * [0]
        pref = n * [0]
        dp[0], pref[0] = nums[0], nums[0]
        dp[1], pref[1] = nums[1], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = pref[i-2] + nums[i]
            pref[i] = max(pref[i-1], dp[i])
        
        return max(dp)