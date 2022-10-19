class Solution:
    def go(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        for i in range(n):
            k = max(self.go(i, i, s), self.go(i, i+1, s))
            if k > len(ans):
                ans = s[i-(k-1)//2:i+k//2+1]
        return ans