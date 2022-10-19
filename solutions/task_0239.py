class SlidingMax:
    def __init__(self, k):
        self.head = []
        self.tail = []
        self.k = k
        self.inf = int(1e9+228)
    
    def get_max(self):
        if len(self.tail) == 0 or len(self.head) == 0:
            res = self.head[-1][1] if len(self.tail) == 0 else self.tail[-1][1]
        else:
            res = max(self.tail[-1][1], self.head[-1][1])
        return res

    def push(self, new_el):
        self.head.append((new_el, new_el)) if len(self.head) == 0 else self.head.append((new_el, max(new_el, self.head[-1][1])))
        if len(self.head) > self.k:
            m = -self.inf
            while len(self.head):
                m = max(m, self.head[-1][0])
                self.tail.append((self.head[-1][0], m))
                self.head.pop()
        if len(self.tail):
            self.tail.pop()

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        ans = []
        window = SlidingMax(k)
        for i in range(n):
            window.push(nums[i])
            if i >= k-1:
                ans.append(window.get_max())
        return ans