# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root, val: int, depth: int):
        
        def dfs(u, d):
            if d == depth-1:
                lt = u.left
                rt = u.right
                u.left = TreeNode(val)
                u.right = TreeNode(val)
                u.left.left = lt
                u.right.right = rt
            if u.left:
                dfs(u.left, d+1)
            if u.right:
                dfs(u.right, d+1)
        
        if depth == 1:
            u = TreeNode(val)
            u.left = root
            u.right = None
            return u
        
        dfs(root, 1)
        return root