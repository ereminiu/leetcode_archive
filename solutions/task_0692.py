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
        print(h)

print(Solution().topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
print(Solution().topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))