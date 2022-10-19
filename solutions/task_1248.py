import bisect

class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        n = len(nums)
        pref = n * [0]
        pref[0] = nums[0] % 2
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]%2
        ans = 0
        for i in range(n):
            w = (0 if i == 0 else pref[i-1]) + k
            ans += bisect.bisect_left(pref, w+1) - bisect.bisect_left(pref, w)
        return ans