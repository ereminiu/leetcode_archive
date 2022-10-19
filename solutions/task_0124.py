# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        
        ans = -int(1e9)
        
        def dfs(u):
            if u == None:
                return 0
            lf = dfs(u.left)
            rg = dfs(u.right)
            nonlocal ans 
            ans = max(ans,max(0, lf) + max(0, rg) + u.val)
            return max(0, lf, rg) + u.val 
        
        dfs(root)
        return ans 