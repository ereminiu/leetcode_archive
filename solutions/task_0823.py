class Solution:
    dp = None
    n = None
    st = None
    MOD = int(1e9 + 7)
    
    def f(self, x, a):
        if self.dp[x] != -1:
            return self.dp[x]
        self.dp[x] = 1
        for k in a:
            if x % k != 0 or k == x:
                continue
            if x//k in self.st:
                self.dp[x] += (self.dp[x//k] * self.dp[k]) % self.MOD
                self.dp[x] %= self.MOD
        return self.dp[x]
    
    def numFactoredBinaryTrees(self, arr) -> int:
        arr.sort()
        self.n = len(arr)
        self.dp = dict((x, -1) for x in arr)
        self.st = set(x for x in arr)
        ans = 0
        for x in arr:
            ans += self.f(x, arr)
            ans %= self.MOD
        return ans