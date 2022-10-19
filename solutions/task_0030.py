from collections import Counter

class Solution:
    def build_h(self, s):
        n = len(s)
        h = n * [0]
        h[0] = ord(s[0])-ord('a')+1
        for i in range(1, n):
            h[i] = ((h[i-1] * self.P) + ord(s[i])-ord('a')+1) % self.MOD
        return h
    
    def build_d(self, n):
        d = (n+1) * [0]
        d[0] = 1
        for i in range(1, n+1):
            d[i] = (d[i-1] * self.P) % self.MOD
        return d

    def get_h(self, l, r):
        return self.h[r] if l == 0 else (self.h[r] - self.h[l-1]*self.deg[r-l+1]) % self.MOD

    def get_hh(self, s):
        result = ord(s[0])-ord('a')+1
        for i in range(1, len(s)):
            result = (result * self.P + ord(s[i]) - ord('a') + 1) % self.MOD
        return result
    
    def findSubstring(self, s: str, words):
        n = len(s)
        m = len(words[0]) * len(words)
        k = len(words[0])
        
        self.MOD = int(1e9+228)
        self.P = 37
        self.h = self.build_h(s)
        self.deg = self.build_d(n)
        
        shouldBe = Counter()
        for i in range(len(words)):
           shouldBe[self.get_hh(words[i])] += 1

        ans = []
        for b in range(n-m+1):
            i = b
            cur = Counter()
            while i <= b+m-1:
                cur[self.get_h(i, i+k-1)] += 1
                i += k
            if cur == shouldBe:
                ans.append(b)
        return ans
            
# s = input()
# words = list(input().split())
# print(Solution().findSubstring(s, words))