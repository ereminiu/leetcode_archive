class Solution:
    def intervalIntersection(self, firstList, secondList):
        n, m = len(firstList), len(secondList)
        empty = [-1, -1]
        
        def intersection(a, b):
            l = max(a[0], b[0])
            r = min(a[1], b[1])
            if l > r:
                return empty
            return [l, r]
        
        ans = []
        p, q = 0, 0
        while p < n and q < m:
            if intersection(firstList[p], secondList[q]) != empty:
                ans.append(intersection(firstList[p], secondList[q]))
            if firstList[p][1] < secondList[q][1]:
                p += 1
            else:
                q += 1
        return ans