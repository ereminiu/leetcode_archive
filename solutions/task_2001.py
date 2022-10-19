from collections import Counter

class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        counter = Counter()
        for r in rectangles:
            counter[r[0]/r[1]] += 1
        # print(*counter)
        ans = 0
        for k in counter:
            ans += counter[k]*(counter[k]-1) // 2
        return ans