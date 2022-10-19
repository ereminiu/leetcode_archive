class Solution:
    def generateParenthesis(self, n: int) -> list:
        
        s = ''
        ans = []

        def f(i, bal, s):
            if i == 2*n:
                nonlocal ans
                ans.append(s)
                return
            if bal > 0:
                f(i+1, bal-1, s+')')
            if bal < 2*n-i:
                f(i+1, bal+1, s+'(')
        f(0, 0, s)
        
        return ans

# print(Solution().generateParenthesis(int(input())))