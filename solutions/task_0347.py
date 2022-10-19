from heapq import*
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        c = Counter()
        for x in nums:
            c[x] += 1
        h = []
        for val in set(nums):
            x, kk = val, c[val]
            heappush(h, (kk, x))
        largest = nlargest(k, h)
        ans = []
        for it in largest:
            ans.append(it[1])
        return ans