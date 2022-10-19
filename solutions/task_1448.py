# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(u, parMax):
            if u.val >= parMax:
                nonlocal ans
                ans += 1
            if u.left != None:
                dfs(u.left, max(parMax, u.val))
            if u.right != None:
                dfs(u.right, max(parMax, u.val))
        
        dfs(root, -int(1e9+228))
        
        return ans