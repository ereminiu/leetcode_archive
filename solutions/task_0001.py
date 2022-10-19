class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        a = []
        for i in range(n):
            a.append((nums[i], i))
        a.sort()
        j = n-1
        for i in range(n):
            while i < j and a[i][0]+a[j][0] >= target:
                if i != j and a[i][0]+a[j][0] == target:
                    return [a[i][1], a[j][1]]
                j -= 1
        assert False