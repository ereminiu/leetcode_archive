class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        ans = 0
        prod = 1
        ans = 0
        left = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right-left+1
        return ans