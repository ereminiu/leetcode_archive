"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        d = []
        
        def dfs(u, depth):
            if u == None:
                return 
            if depth > len(d):
                d.append([u.val])
            else:
                d[depth-1].append(u.val)
            if u.children == None:
                return
            for v in u.children:
                dfs(v, depth+1)
        
        dfs(root, 1)
        
        return d