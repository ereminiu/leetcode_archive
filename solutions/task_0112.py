# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        ok = False 
        
        def dfs(u, sum):
           # print(sum)
            if not u.left and not u.right:
                if sum == targetSum:
                    nonlocal ok
                    ok = True 
            if u.left:
                dfs(u.left, sum+u.left.val)
            if u.right:
                dfs(u.right, sum+u.right.val)
        if not root:
            return False
        dfs(root, root.val)
        return ok