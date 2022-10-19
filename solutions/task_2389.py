from bisect import bisect_left

class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        n = len(nums)
        pref = n * [0]
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]
        ans = []
        for q in queries:
            idx = bisect_left(pref, q)
            if idx == n:
                ans.append(idx)
            else:
                if pref[idx] <= q:
                    ans.append(idx+1)
                else:
                    ans.append(idx)
        return ans