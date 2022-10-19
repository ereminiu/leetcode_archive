class Solution:
    def findSubarrays(self, nums) -> bool:
        st = set()
        for i in range(len(nums)-1):
            sum = nums[i]+nums[i+1]
            if sum in st:
                return True
            st.add(sum)
        return False