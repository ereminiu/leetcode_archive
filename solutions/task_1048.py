class Solution:
    def f(self, s):
        if len(s) == 1:
            return 1
        if self.memo[s] != -1:
            return self.memo[s]
        result = 0
        for i in range(len(s)):
            t = s[0:i]+s[i+1:len(s)]
            if t in self.st:
                result = max(result, self.f(t))
        self.memo[s] = result+1
        return result+1

    def longestStrChain(self, words) -> int:
        self.st = set()
        self.memo = dict()
        for w in words:
            self.memo[w] = -1
            self.st.add(w)
        ans = 0
        for s in self.st:
            ans = max(ans, self.f(s))
        return ans   

# print(Solution().longestStrChain(list(input().split())))
# print(Solution().longestStrChain(words=["abcd","dbqca"]))