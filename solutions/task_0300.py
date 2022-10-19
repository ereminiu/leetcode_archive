import bisect 

class Solution:
    def lengthOfLIS(self, nums) -> int:
        state = []
        for x in nums:
            idx = bisect.bisect_left(state, x)
            if idx == len(state):
                state.append(x)
            else:
                state[idx] = x
        return len(state)