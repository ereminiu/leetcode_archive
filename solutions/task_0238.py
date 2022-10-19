class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        pref = n * [0]
        suff = n * [0]
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i]
        suff[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]
        ans = []
        for i in range(n):
            me = 1
            if i > 0:
                me *= pref[i-1]
            if i < n-1:
                me *= suff[i+1]
            ans.append(me)
        return ans