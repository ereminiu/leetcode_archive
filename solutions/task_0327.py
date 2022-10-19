import bisect

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.t = n * [0]

    def f(self, i): return i & (i+1)
    def g(self, i): return i | (i+1)

    def sum(self, r):
        result = 0
        while r >= 0:
            result += self.t[r]
            r = self.f(r)-1
        return result

    def modify(self, i, d):
        while i < self.n:
            self.t[i] += d
            i = self.g(i)

    def get_sum(self, l, r):
        return self.sum(r) if l == 0 else self.sum(r)-self.sum(l-1)

    def __repr__(self):
        res = ''
        for i in range(self.n):
            res += repr(self.get_sum(i, i))
        return res

class Solution:
    def countRangeSum(self, a, lower: int, upper: int) -> int:
        n = len(a)
        pref = n * [0]
        pref[0] = a[0]
        for i in range(n):
            pref[i] = pref[i-1] + a[i]
        order = sorted(list(set(pref)))
        m = len(order)
        tr = Fenwick(m)
        sum = 0; ans = 0
        for i in range(n):
            sum += a[i]
            r = bisect.bisect_right(order, sum - lower)-1; l = bisect.bisect_left(order, sum - upper)
            ans += tr.get_sum(l, r)
            if lower <= sum <= upper:
                ans += 1
            tr.modify(bisect.bisect_left(order, sum), 1)
        return ans
            

# a = list(map(int, input().split()))
# lower, upper = map(int, input().split())
# print(Solution().countRangeSum(a, lower, upper))