class Histogram:
    def largestRect(self, heights) -> int:
        heights.append(0)
        n = len(heights)
        st = []
        ans = 0
        for i in range(n):
            h = heights[i]
            while len(st) and heights[st[-1]] > h:
                H = heights[st.pop()]
                W = i
                if len(st) > 0:
                    W = i-st[-1]-1
                ans = max(ans, H*W)
            st.append(i)
                
        return ans

class Solution:
    def maximalRectangle(self, matrix) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m-1, -1, -1):
                if matrix[i][j] == '0':
                    continue
                if j == m-1:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i][j+1] + 1
        ans = 0
        for i in range(m):
            h = []
            for j in range(n):
                h.append(dp[j][i])
            # print(*h, Histogram().largestRect(h))
            ans = max(ans, Histogram().largestRect(h))
        return ans