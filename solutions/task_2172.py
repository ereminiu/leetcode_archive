class Solution:
    def maximumANDSum(self, nums, numSlots: int) -> int:
        n = len(nums)
        dp = [[0 for x in range(2**n+1)] for y in range(numSlots+1)]
        
        for i in range(1, numSlots+1):
            for mask in range(2**n):
                dp[i][mask] = dp[i-1][mask]
                for j in range(n):
                    if not mask & (2**j):
                        continue
                    dp[i][mask] = max(dp[i][mask], dp[i-1][mask ^ (2**j)] + (nums[j] & i))
                    for k in range(n):
                        if k == j:
                            continue
                        if mask & (2**j) and mask & (2**k):
                            dp[i][mask] = max(dp[i][mask], dp[i-1][mask ^ (2**j | 2**k)] + (nums[j] & i) + (nums[k]&i))
        # print(dp[1][9])
        # # sum = 0
        # # for i in range(n):
        # #     if 9 & (2**i):
        # #         sum += nums[i] & 1
        # # print(sum)
        return dp[numSlots][2**n-1]

print(Solution().maximumANDSum(nums = [1,2,3,4,5,6], numSlots = 3))
print(Solution().maximumANDSum(nums = [1,3,10,4,7,1], numSlots = 9))