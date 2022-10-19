class Solution:
    def garbageCollection(self, garbage, travel) -> int:
        n = len(garbage)
        ans = 0
        last = 3 * [0]
        types = ['M', 'P', 'G']
        for i in range(n):
            for j in range(3):
                if types[j] in garbage[i]:
                    last[j] = i
            for c in garbage[i]:
                ans += len(c)
        for i in range(3):
            for j in range(last[i]):
                ans += travel[j]
        return ans