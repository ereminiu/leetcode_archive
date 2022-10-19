class Solution:
    def maxCoins(self, nums) -> int:
        
        def solve(l, r):
            if l > r:
                return 0
            if memo[l][r] != -1:
                return memo[l][r]          
            ret = 0
            for i in range(l, r+1):
                cur = nums[l-1] * nums[i] * nums[r+1] + solve(l, i-1) + solve(i+1, r)
                ret = max(ret, cur)
            memo[l][r] = ret
            return ret
        
        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[-1 for x in range(n+1)] for y in range(n+1)]
        return solve(1, n-2)