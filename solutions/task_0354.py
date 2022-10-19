import bisect

class Solution:    
    def maxEnvelopes(self, envelopes) -> int:
        class Pair:
            def __init__(self, a, b):
                self.a = a
                self.b = b

            def __lt__(self, other):
                if self.a == other.a:
                    return self.b > other.b
                return self.a < other.a
        
        n = len(envelopes)
        pairs = n * [Pair(0, 0)]
        for i in range(n):
            pairs[i] = Pair(envelopes[i][0], envelopes[i][1])
        pairs.sort()
        inf = int(1e9+228)
        w = []
        for i in range(n):
            w.append(pairs[i].b)
        n = len(w)

        def LIS():
            state = []
            state.append(w[0])
            for i in range(1, n):
                if w[i] > state[-1]:
                    state.append(w[i])
                else:
                    idx = bisect.bisect_left(state, w[i])
                    state[idx] = w[i]
            return len(state)
        
        return LIS()