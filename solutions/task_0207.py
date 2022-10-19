class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        n = numCourses
        gr = []
        for i in range(n):
            gr.append([])
        for e in prerequisites:
            gr[e[0]].append(e[1])
        col = n * [0]
        
        ok = True
        
        def dfs(u):
            col[u] = 1
            for v in gr[u]:
                if col[v] == 1:
                    nonlocal ok
                    ok = False
                if col[v] == 0:
                    dfs(v)
            col[u] = 2
        
        for i in range(n):
            if not col[i]:
                dfs(i)
        
        return ok