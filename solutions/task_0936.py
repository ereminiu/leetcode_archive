from collections import deque

class Solution:
    def movesToStamp(self, stamp: str, target: str):
        m, n = len(stamp), len(target)
        dq = deque()
        u = [False] * n
        ans = []
        a = []
        for i in range(n-m+1):
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                cur = target[i+j]
                if cur == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            a.append((made, todo))
            if len(todo) == 0:
                ans.append(i)
                for j in range(i, i+len(stamp)):
                    if not u[j]:
                        dq.append(j)
                        u[j] = True
        while len(dq):
            i = dq.popleft()
            for j in range(max(0, i-m+1), min(n-m, i)+1):
                if i in a[j][1]:
                    a[j][1].discard(i)
                    if not a[j][1]:
                        ans.append(j)
                        for M in a[j][0]:
                            if not u[M]:
                                dq.append(M)
                                u[M] = True
        return ans[::-1] if all(u) else []

# print(Solution().movesToStamp(stamp='abca', target='aabcaca'))