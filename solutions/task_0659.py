from collections import Counter

class Solution:
    def isPossible(self, nums) -> bool:
        c = Counter(nums)
        e = Counter()
        for x in nums:
            if c[x]:
                c[x] -= 1
                if e[x-1] > 0:
                    e[x] += 1
                    e[x-1] -= 1
                elif c[x+1] > 0 and c[x+2] > 0:
                    c[x+1] -= 1
                    c[x+2] -= 1
                    e[x+2] += 1
                else:
                    return False
        return True

# print(Solution().isPossible(list(map(int, input().split()))))