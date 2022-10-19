from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        
        P = 31
        MOD = int(1e9+7)
        
        def get_code(s):
            res = 0
            for c in sorted(s):
                res = (res * P + ord(c)) % MOD
            return res
        pairs = []
        for s in strs:
            pairs.append((get_code(s), s))
        pairs.sort()
        ans = []
        prev = -MOD
        n = len(strs)
        for i in range(n):
            if pairs[i][0] != prev:
                ans.append([pairs[i][1]])
            else:
                ans[-1].append(pairs[i][1])
            prev = pairs[i][0]
        return ans