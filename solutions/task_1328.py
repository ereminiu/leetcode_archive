class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        pz = -1
        s = list(palindrome)
        n = len(s)
        for i in range(n):
            if s[i] != 'a' and not (n%2 == 1 and i == n//2):
                pz = i
                break 
        if pz == -1:
            s[n-1] = 'b' 
        else:
            s[pz] = 'a' 
        return ''.join(s)