# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k: int) -> bool:
        
        st = set()
        
        def dfs(u):
            nonlocal st
            st.add(u.val)
            if u.left:
                dfs(u.left)
            if u.right:
                dfs(u.right)
        
        dfs(root)
        # print(st)
        
        for x in st:
            if 2*x != k and k-x in st:
                return True
        
        return False