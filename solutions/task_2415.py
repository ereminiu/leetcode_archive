# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def reverseOddLevels(self, root):
        
        q = deque()
        q.appendleft((root, 0))
        vals = [[root.val]]
        nodes = [[root]]
        while q:
            u, k = q.pop()
            if u.left:
                q.appendleft((u.left, k+1))
                if k+1 >= len(vals):
                    vals.append([u.left.val])
                    nodes.append([u.left])
                else:
                    vals[-1].append(u.left.val)
                    nodes[-1].append(u.left)
            if u.right:
                q.appendleft((u.right, k+1))
                if k+1 >= len(vals):
                    vals.append([u.right.val])
                    nodes.append([u.right])
                else:
                    vals[-1].append(u.right.val)
                    nodes[-1].append(u.right)
        
        for i in range(len(vals)):
            if i % 2 == 0:
                continue
            vl = vals[i][::-1]
            for j in range(len(nodes[i])):
                nodes[i][j].val = vl[j]
        
        return root