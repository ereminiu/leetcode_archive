from math import gcd
from collections import Counter

class Solution:
    def maxPoints(self, points) -> int:
        
        def get(p, q):
            a, b = p[1]-q[1], q[0]-p[0],
            c = -a*p[0] - b*p[1]
            gc = gcd(abs(a), abs(b), abs(c))
            a //= gc; b //= gc; c //= gc
            if a < 0 or (a == 0 and b < 0):
                a *= -1; b *= -1; c *= -1
            return (a, b, c)
        
        n = len(points)
        counter = Counter()
        mx = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                vl = get(points[i], points[j])
                counter[vl] += 1
                mx = max(mx, counter[vl])
        return int(max(1, (1+(1+4*mx)**0.5) // 2))