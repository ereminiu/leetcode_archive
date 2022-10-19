import bisect

class SegTree:
    def __init__(self, a):
        self.n = len(a)
        self.lz = (4*self.n) * [-1] #Keep your attention at the neutral val
        self.t = (4*self.n) * [0]
        self.build(0, 0, self.n, a)

    def push(self, v, vl, vr):
        if self.lz[v] == -1:
            return
        self.t[v] = self.lz[v]
        if vl != vr-1:
            self.lz[2*v+1] = self.lz[v]
            self.lz[2*v+2] = self.lz[v]
        self.lz[v] = -1
    
    def build(self, v, vl, vr, a):
        if vl == vr-1:
            self.t[v] = a[vl]
            return
        mid = (vl+vr)//2
        self.build(2*v+1, vl, mid, a)
        self.build(2*v+2, mid, vr, a)
        self.t[v] = max(self.t[2*v+1], self.t[2*v+2])
    
    def max(self, v, vl, vr, l, r):
        self.push(v, vl, vr)
        if l >= vr or r <= vl:
            return 0
        if vl >= l and r >= vr:
            return self.t[v]
        mid = (vl+vr)//2
        return max(self.max(2*v+1, vl, mid, l, r), self.max(2*v+2, mid, vr, l, r))
    
    def changeAt(self, v, vl, vr, l, r, x):
        self.push(v, vl, vr)
        if l >= vr or r <= vl:
            return
        if vl >= l and r >= vr:
            self.lz[v] = x
            self.push(v, vl, vr)
            return
        mid = (vl+vr)//2
        self.changeAt(2*v+1, vl, mid, l, r, x)
        self.changeAt(2*v+2, mid, vr, l, r, x)
        self.t[v] = max(self.t[2*v+1], self.t[2*v+2])
    
    def __repr__(self):
        ret = ''
        for i in range(self.n):
            ret += repr(self.max(0, 0, self.n, i, i+1))
            ret += ' '
        return ret

class Event:
    def __init__(self, l, r, h):
        self.l = l
        self.r = r
        self.h = h
    
    def __lt__(self, other):
        return (self.h < other.h) or (self.h == other.h and self.l < other.h)

    def __repr__(self):
        return repr(self.l)+' '+repr(self.r)+' '+repr(self.h)

class Solution:    
    def getSkyline(self, buildings):
        n = len(buildings)
        coordX = []
        events = n * [Event(0, 0, 0)]
        for i in range(n):
            events[i] = Event(buildings[i][0], buildings[i][1], buildings[i][2])
            coordX.append(buildings[i][0])
            coordX.append(buildings[i][1])
        order = list(sorted(set(coordX)))
        events.sort()
        m = len(order)
        st = SegTree(m * [0])
        for ev in events:
            l, r, h = ev.l, ev.r, ev.h
            l = bisect.bisect_left(order, l)
            r = bisect.bisect_left(order, r)
            st.changeAt(0, 0, m, l, r, h)
        ans = [[order[0], st.max(0, 0, m, 0, 1)]]
        prev = st.max(0, 0, m, 0, 1)
        for i in range(1, m):
            val = st.max(0, 0, m, i, i+1)
            if val != prev:
                ans.append([order[i], val])
            prev = val
        return ans

# n = int(input())
# buildings = [[0 for x in range(3)] for y in range(n)]
# for i in range(n):
#     buildings[i] = list(map(int, input().split()))
# print(Solution().getSkyline(buildings=[[0,2,3],[2,5,3]]))