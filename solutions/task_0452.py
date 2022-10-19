class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort()
        prev = points[0]
        ans = 1
        for s, e in points[1:]:
            if s > prev[1]:
                prev = [s, e]
                ans += 1
            else:
                prev[1] = min(prev[1], e)
        
        return ans

# print(Solution().findMinArrowShots(points=[[10,16],[2,8],[1,6],[7,12]]))