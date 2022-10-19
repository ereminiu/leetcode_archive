# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):
        
        def go(u, val):
            if val > u.val:
                if not u.right:
                    u.right = TreeNode(val)
                    return
                go(u.right, val)
            else:
                if not u.left:
                    u.left = TreeNode(val)
                    return
                go(u.left, val)
        
        if not root:
            return TreeNode(val)

        go(root, val)
        return root