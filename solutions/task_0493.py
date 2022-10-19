import bisect

class Tree:
    def __init__(self, a):
        self.n = len(a)
        self.a = a
        self.t = [0] * self.n
        # self.build

    def f(self, i): return i & (i+1)
    def g(self, i): return i | (i+1)

    def modify(self, i, d):
        while i < self.n:
            self.t[i] += d
            i = self.g(i)

    def set(self, i, x):
        d = x-self.a[i]
        self.a[i] = x
        self.modify(i, d)

    def sum(self, i):
        ret = 0
        while i >= 0:
            ret += self.t[i]
            i = self.f(i)-1
        return ret

    def build(self):
        for i in range(self.n):
            self.modify(i, self.a[i])

    def get_sum(self, l, r):
        if l == 0:
            return self.sum(r)
        return self.sum(r)-self.sum(l-1)

    def __repr__(self) -> str:
        ret = ''
        for i in range(self.n):
            ret += repr(self.get_sum(i, i))
        return ret

class Solution:
    def reversePairs(self, nums) -> int:
        a = nums
        order = sorted(list(set(sorted(a))))
        n = len(a)
        tr = Tree(n*[0])
        ans = 0
        for i in range(n):
            idx = bisect.bisect_left(order, 2*a[i] + 1)
            if idx < n:
                ans += tr.get_sum(idx, n-1)
            tr.modify(bisect.bisect_left(order, a[i]), 1)
        return ans

# print(Solution().reversePairs(list(map(int, input().split())))) 