# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        depth = []
        count = []
        
        def dfs(u, curdepth):
            if curdepth > len(depth):
                depth.append(0)
                count.append(0)
            depth[curdepth-1] += u.val
            count[curdepth-1] += 1
            if u.left != None:
                dfs(u.left, curdepth+1)
            if u.right != None:
                dfs(u.right, curdepth+1)
        
        dfs(root, 1)
        
        return list(map(lambda i: depth[i]/count[i], range(len(depth))))