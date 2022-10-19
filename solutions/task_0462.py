class Solution:
    def minMoves2(self, nums) -> int:
        nums.sort()
        n = len(nums)
        pref = n * [0]
        suff = n * [0]
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]
        suff[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] + nums[i]
        ans = int(1e18+111111)
        for i in range(n):
            cur = 0
            if i > 0:
                cur += nums[i]*i - pref[i-1]
            if i < n-1:
                cur += suff[i+1] - nums[i]*(n-i-1)
            ans = min(ans, cur)
        return ans