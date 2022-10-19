class Solution:
    def largestRectangleArea(self, heights) -> int:
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