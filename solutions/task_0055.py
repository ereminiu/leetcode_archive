class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        suff = n * [0]
        suff[n-1] = 1
        
        def get_sum(l, r):
            return suff[l] if r == n-1 else suff[l] - suff[r+1]
        
        for i in range(n-2, -1, -1):
            j = min(i+nums[i], n-1)
            if get_sum(i+1, j) > 0:
                suff[i] = 1 + suff[i+1]
            else:
                suff[i] = suff[i+1]
        return get_sum(0, min(n-1, nums[0])) > 0