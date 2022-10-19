from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        shouldBe = 26 * [0]
        state = 26 * [0]
        for i in range(len(p)):
            shouldBe[ord(p[i])-ord('a')] += 1
            state[ord(s[i])-ord('a')] += 1
        ans = []
        if state == shouldBe:
            ans.append(0)
        for i in range(len(p), len(s)):
            state[ord(s[i-len(p)])-ord('a')] -= 1
            state[ord(s[i]) - ord('a')] += 1
            if state == shouldBe:
                ans.append(i-len(p)+1)
        return ans
