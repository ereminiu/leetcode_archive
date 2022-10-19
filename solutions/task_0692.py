from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k: int):
        counter = Counter()
        for s in words:
            counter[s] += 1
        h = []
        for s in set(words):
            heapq.heappush(h, (counter[s], s))
        ans = []
        for r in range(k):
            ans.append(heapq.heappop(h))
        return ans