import bisect

class Fenwick:
    def __init__(self, a):
        self.a = a
        self.n = len(a)
        self.t = [0] * self.n
        self.build()
    
    def f(self, x): return x & (x+1)
    def g(self, x): return x | (x+1)

    def modify(self, i, d):
        while i < self.n:
            self.t[i] += d
            i = self.g(i)
    
    def set(self, i, x):
        d = x-self.a[i]
        self.a[i] = x
        self.modify(i, d)
    
    def sum(self, r):
        res = 0
        while r >= 0:
            res += self.t[r]
            r = self.f(r) - 1
        return res
    
    def get_sum(self, l, r):
        return self.sum(r) if l == 0 else self.sum(r) - self.sum(l-1)

    def build(self):
        for i in range(self.n):
            self.modify(i, self.a[i])

class Solution:
    def countSmaller(self, nums):
        order = sorted(list(set(nums)))
        n = len(nums)
        m = len(order)
        count = n * [0]
        tr = Fenwick(m * [0])
        for i in range(n):
            idx = bisect.bisect_left(order, nums[i])
            tr.modify(idx, 1)
        for i in range(n):
            idx = bisect.bisect_left(order, nums[i])
            tr.modify(idx, -1)
            count[i] = tr.sum(idx-1)
        return count

# print(Solution().countSmaller(list(map(int, input().split()))))n