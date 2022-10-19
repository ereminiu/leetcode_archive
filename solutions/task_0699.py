from bisect import bisect_left

class SegTree:
    def __init__(self, n):
        self.inf = -1
        self.N = n
        self.t = 4*n * [0]
        self.lz = 4*n * [self.inf]
    
    def push(self, v, vl, vr):
        if self.lz[v] == self.inf:
            return
        self.t[v] = self.lz[v]
        if vl != vr-1:
            self.lz[2*v+1] = self.lz[v]
            self.lz[2*v+2] = self.lz[v]
        self.lz[v] = self.inf
    
    def max(self, v, vl, vr, l, r):
        self.push(v, vl, vr)
        if vl >= r or vr <= l:
            return 0
        if vl >= l and vr <= r:
            return self.t[v]
        mid = (vl+vr) // 2
        al, ar = self.max(2*v+1, vl, mid, l, r), self.max(2*v+2, mid, vr, l, r)
        return max(al, ar)
    
    def set(self, v, vl, vr, l, r, x):
        self.push(v, vl, vr)
        if vl >= r or vr <= l:
            return
        if vl >= l and vr <= r:
            self.lz[v] = x
            self.push(v, vl, vr)
            return
        mid = (vl+vr) // 2
        self.set(2*v+1, vl, mid, l, r, x)
        self.set(2*v+2, mid, vr, l, r, x)
        self.t[v] = max(self.t[2*v+1], self.t[2*v+2])
    
    def __repr__(self):
        ret = ''
        for i in range(self.N):
            ret += repr(self.max(0, 0, self.N, i, i+1)) + ' '
        return ret 

class Solution:
    def fallingSquares(self, positions):
        n = len(positions)
        coords = set()
        for i in range(n):
            coords.add(positions[i][0])
            coords.add(positions[i][0]+positions[i][1])
        
        order = list(sorted(coords))
        m = len(order)
        tree = SegTree(m)
        ans = []
        for segment in positions:
            l, r = bisect_left(order, segment[0]), bisect_left(order, segment[0]+segment[1])
            if l == r:
                r += 1
            new_val = tree.max(0, 0, m, l, r)+segment[1]
            tree.set(0, 0, m, l, r, new_val)
            ans.append(tree.max(0, 0, m, 0, m))
        
        return ans