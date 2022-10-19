class Solution:
    def letterCombinations(self, digits: str) -> list:
        dc = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        ans = []

        def go(k, s):
            if k == n:
                ans.append(''.join(s))
                return
            for c in dc[digits[k]]:
                s.append(c)
                go(k+1, s)
                s.pop()
        if not digits:
            return []
        
        for c in dc[digits[0]]:
            go(1, [c])

        return ans

# print(Solution().letterCombinations(input()))