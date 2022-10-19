from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 10:
            return []
        
        n = len(s)
        counter = Counter()
        for i in range(n-9):
            counter[s[i:i+10]] += 1
        ans = []
        for u in counter:
            if counter[u] > 1:
                ans.append(u)
        return ans