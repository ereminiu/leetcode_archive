class Solution:
    def combinationSum(self, candidates, target: int):
        
        ans = []
        def go(sum, path, k):
            if sum == target:
                nonlocal ans
                ans.append(path[::])
            for i in range(k, len(candidates)):
                if sum+candidates[i] <= target:
                    path.append(candidates[i])
                    go(sum+candidates[i], path, i)
                    path.pop()
        
        go(0, [], 0)

        return ans

# print(Solution().combinationSum(candidates = [2,3,5], target = 8))