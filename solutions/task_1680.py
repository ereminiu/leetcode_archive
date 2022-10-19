class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        mod = int(1e9+7)
        power = 1
        size = 0
        for i in range(1, n+1):
            size += (i & (i-1)) == 0
            ans = ((ans << size) + i) % mod
        return ans

# print(Solution().concatenatedBinary(int(input())))