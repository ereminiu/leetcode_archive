from collections import Counter

class Solution:
    def minSetSize(self, arr) -> int:
        n = len(arr)
        counter = Counter()
        for k in arr:
            counter[k] += 1
        c = []
        for x in set(arr):
            c.append(counter[x])
        c.sort()
        cur = 0
        k = 0
        for i in range(len(c)-1, -1, -1):
            if cur >= (n+1)//2:
                break
            cur += c[i]
            k += 1
        return k

# print(Solution().minSetSize(list(map(int, input().split()))))