class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        f = n * [1]
        for i in range(n):
            if f[i] != 1:
                continue
            p = alphabet.index(s[i])
            j = i
            while j < n and p < len(alphabet) and s[j] == alphabet[p]:
                j += 1
                p += 1
            f[i] = j-i
        return max(f)
