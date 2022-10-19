class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        l = 0
        sum = 0
        n = len(nums)
        ans = int(1e9+111)
        for r in range(n):
            sum += nums[r]
            while l <= r and sum >= target:
                ans = min(ans, r-l+1)
                sum -= nums[l]
                l += 1
        return 0 if ans == int(1e9+111) else ans