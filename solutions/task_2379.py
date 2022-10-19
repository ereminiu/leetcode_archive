class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        pref = n * [0]
        pref[0] = 1 if blocks[0] == 'W' else 0
        for i in range(1, n):
            pref[i] = pref[i-1]
            if blocks[i] == 'W':
                pref[i] += 1
        ans = int(1e9+228)
        for i in range(n-k+1):
            cur = pref[i+k-1]
            if i > 0:
                cur -= pref[i-1]
            ans = min(ans, cur)
        return ans