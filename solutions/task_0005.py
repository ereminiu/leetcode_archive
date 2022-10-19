class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)
        
        def go(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            nonlocal ans
            if r-l-1 > len(ans):
                ans = s[l+1:r]
        
        for i in range(n):
            go(i, i)
            go(i, i+1)
        
        return ans