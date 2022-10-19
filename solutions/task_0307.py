class BIT:
    def __init__(self, n):
        self.t = n * [0]
        self.a = n * [0]
        self.N = n
    
    def f(self, x):
        return x & (x+1)
    
    def g(self, x):
        return x | (x+1)

    def pref(self, i):
        res = 0
        while i >= 0:
            res += self.t[i]
            i = self.f(i)-1
        return res
    
    def modify(self, i, x):
        self.a[i] += x
        while i < self.N:
            self.t[i] += x
            i = self.g(i)
    
    def set(self, i, val):
        x = val-self.a[i]
        self.modify(i, x)
    
    def sum(self, l, r):
        return self.pref(r) if l == 0 else self.pref(r) - self.pref(l-1)
    
    def __repr__(self):
        ret = ''
        for i in range(self.N):
            ret += repr(self.sum(i, i)) + ' '
        return ret

class NumArray:

    def __init__(self, nums):
        self.tree = BIT(len(nums))
        n = len(nums)
        for i in range(n):
            self.tree.modify(i, nums[i])

    def update(self, index: int, val: int) -> None:
        self.tree.set(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)