class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        n = len(intervals)
        u = n * [False]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    u[i] = True
        ans = 0
        for i in range(n):
            ans += not u[i]
        return ans

# print(Solution().removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]]))