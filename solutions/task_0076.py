from collections import Counter

class Solution:
    def ok(self, dict_s, dict_t) -> bool:
        for c in dict_t:
            if dict_s[c] < dict_t[c]:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        dict_s = Counter()
        dict_t = Counter()
        for c in t:
            dict_t[c] += 1
        ans = ''
        l = 0
        for r in range(n):
            dict_s[s[r]] += 1
            while l <= r and self.ok(dict_s, dict_t):
                if ans == '' or r-l+1 < len(ans):
                    ans = s[l:r+1]
                dict_s[s[l]] -= 1
                l += 1
        return ans

# s, t = input().split()
# print(Solution().minWindow(s, t))