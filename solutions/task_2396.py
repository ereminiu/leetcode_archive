class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def ispal(x, base):
            p = []
            while x > 0:
                p.append(x%base)
                x //= base
            return p == p[::-1]
        
        for base in range(2, n-1):
            if not ispal(n, base):
                return False
        
        return True