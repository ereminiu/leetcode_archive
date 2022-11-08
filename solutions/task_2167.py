class Solution:
    def minimumTime(self, s: str) -> int:
        if s == '0': 
            return 0
        n = len(s)
        pref = n * [0]
        suf = n * [0]
        pref[0], suf[n-1] = ord(s[0])-ord('0'), ord(s[n-1])-ord('0')
        for i in range(1, n):
            pref[i] = pref[i-1] if s[i] == '0' else min(pref[i-1]+2, i+1)
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] if s[i] == '0' else min(suf[i+1]+2, n-i)
        ans = pref[0]+(0 if n == 1 else suf[1])
        for i in range(n-1):
            ans = min(ans, pref[i]+suf[i+1])
        return ans

print(Solution().minimumTime(s = "1100101"))
print(Solution().minimumTime(s = "1"))