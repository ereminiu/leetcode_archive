# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        a = []
        
        def go(u):
            a.append(u.val)
            if u.left:
                go(u.left)
            if u.right:
                go(u.right)
        go(root)
        
        a.sort()
        return a[k-1]