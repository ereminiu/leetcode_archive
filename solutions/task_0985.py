class Solution:
    def sumEvenAfterQueries(self, nums: list, queries: list) -> list:
        sum = 0
        for x in nums:
            if x % 2 == 0:
                sum += x
        ans = []
        for [x, i] in queries:
            if (nums[i] + x) % 2:
                if nums[i] % 2 == 0:
                    sum -= nums[i]
            else:
                if nums[i] % 2 == 0:
                    sum += x
                else:
                    sum += nums[i]+x
            nums[i] += x
            ans.append(sum)
        return ans

# print(Solution().sumEvenAfterQueries(nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))