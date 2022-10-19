class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n-1
        while left < right:
            h = min(height[left], height[right])
            w = right-left
            ans = max(ans, h*w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans