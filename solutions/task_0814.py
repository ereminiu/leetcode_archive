# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root):
        
        def dfs(u):
            w = u.val
            if u.left:
                lf = dfs(u.left)
                if not lf:
                    u.left = None 
                w += lf
            if u.right:
                rg = dfs(u.right)
                if not rg:
                    u.right = None 
                w += rg 
            return w 
        
        if not dfs(root):
            root = None
        return root
            