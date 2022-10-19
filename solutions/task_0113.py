# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int):
        ans = []
        
        def dfs(u, sum, path):
            if u.val+sum == targetSum and not (u.left or u.right):
                ans.append(path[::]+[u.val])
                return
            if u.right:
                path.append(u.val)
                dfs(u.right, sum+u.val, path)
                path.pop()
            if u.left:
                path.append(u.val)
                dfs(u.left, sum+u.val, path)
                path.pop()
                
        if not root:
            return []
        dfs(root, 0, [])
        return ans