# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        
        def ispal(count):
            odd = 0
            for c in count:
                odd += c % 2
            return odd < 2
        
        ans = 0
        
        def dfs(u, count):
            count[u.val] += 1
            if not u.left and not u.right and ispal(count):
                nonlocal ans
                ans += 1
            if u.left:
                dfs(u.left, count)
            if u.right:
                dfs(u.right, count)
            count[u.val] -= 1
        
        count = 10 * [0]
        dfs(root, count)
        return ans