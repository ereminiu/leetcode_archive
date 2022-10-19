class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        alphabet = len(set(c for c in s))
        for i in range(n):
            st = set()
            for j in range(i, min(n, i+alphabet+1)):
                if s[j] in st:
                    break
                ans = max(ans, j-i+1)
                st.add(s[j])
        return ans