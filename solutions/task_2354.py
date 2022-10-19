import math
import bisect

class Solution:
    def count(self, x):
        ret = 0
        while x > 0:
            if x % 2 == 1:
                ret += 1
            x //= 2
        return ret
    
    def countExcellentPairs(self, nums, k: int) -> int:
        nums = list(set(nums))
        n = len(nums)
        bitCount = n * [0]
        for i in range(n):
            bitCount[i] = self.count(nums[i])
        bitCount.sort()
        ans = 0
        for i in range(n):
            ans += n-bisect.bisect_left(bitCount, k-bitCount[i])
        return ans