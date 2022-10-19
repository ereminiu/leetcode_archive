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
    def constrainedSubsetSum(self, nums, k: int) -> int:
        n = len(nums)
        window = SlidingMax(k)
        window.push(nums[0])
        dp = n * [0]
        ans = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(0, window.get_max())
            window.push(dp[i])
            ans = max(ans, dp[i])
        # print(dp)
        return ans

# nums = list(map(int, input().split()))
# k = int(input())
# print(Solution().constrainedSubsetSum(nums, k))