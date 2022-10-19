class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        ans = 0
        while '01' in s:
            pz = []
            for i in range(n-1):
                if s[i]+s[i+1] == '01':
                    pz.append(i)
            new = list(s)
            for i in pz:
                new[i], new[i+1] = '1', '0'
            s = ''.join(new)
            ans += 1
        return ans

# print(Solution().secondsToRemoveOccurrences(input()))