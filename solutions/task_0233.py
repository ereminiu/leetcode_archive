class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        k = 1
        while k <= n:
            d = 10 * k
            ans += (n // d) * k + min(max(n%d - k + 1, 0), k)
            k *= 10
        return ans

# print(Solution().countDigitOne(int(input())))