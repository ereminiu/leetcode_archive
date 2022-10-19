class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        n = len(intervals)
        ans = n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    ans -= 1
                    break
        return ans