class Solution:
    def countTime(self, time: str) -> int:
        def transform(x):
            h = x // 60
            m = x % 60
            return repr(h).rjust(2, '0') + ':' + repr(m).rjust(2, '0')
        
        ans = 0
        for x in range(0, 1440):
            f = transform(x)
            fl = True
            for i in range(5):
                if f[i] != time[i] and time[i] != '?':
                    fl = False
                    break
            ans += fl
        return ans