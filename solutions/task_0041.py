class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        valid = (n+2) * [False]
        for x in nums:
            if x > 0 and x <= n:
                valid[x] = True
        for i in range(1, n+2):
            if not valid[i]:
                return i