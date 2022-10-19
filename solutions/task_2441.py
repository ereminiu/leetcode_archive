class Solution:
    def findMaxK(self, nums) -> int:
        neg = set()
        for x in nums:
            neg.add(x)
        ans = -1
        for x in nums:
            if x > 0 and -x in neg:
                ans = max(ans, x)
        return ans