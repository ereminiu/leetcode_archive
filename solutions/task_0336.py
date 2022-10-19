from collections import Counter

class Solution:
    def palindromePairs(self, words):
        rev = Counter()
        n = len(words)
        for i in range(n):
            rev[words[i][::-1]] = i
        
        ans = []
        for i in range(n):
            w = words[i]
            if w in rev and rev[w] != i:
                ans.append([i, rev[w]])
            
            if w != '' and '' in rev and w == w[::-1]:
                ans.append([i, rev['']])
                ans.append([rev[''], i])
            
            for j in range(len(w)):
                if w[j:] in rev and w[:j] == w[j-1::-1]:
                    ans.append([rev[w[j:]], i])
                if w[:j] in rev and w[j:] == w[:j-1:-1]:
                    ans.append([i, rev[w[:j]]])
        
        return ans