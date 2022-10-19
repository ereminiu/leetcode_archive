class Solution:
    def make(self, s):
        ans = []
        for c in s:
            if c != '#':
                ans.append(c)
            elif len(ans) != 0:
                ans.pop()
        return ans
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.make(s) == self.make(t)