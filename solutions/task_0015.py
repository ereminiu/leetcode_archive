import bisect

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        st = set()
        for i in range(n):
            for j in range(i+1, n):
                idx = bisect.bisect_right(nums, -(nums[i]+nums[j]))-1
                if nums[idx] == -(nums[i]+nums[j]) and idx > j:
                    st.add((nums[i], nums[j], nums[idx]))
        ans = []
        for me in st:
            ans.append(list(me))
        return ans