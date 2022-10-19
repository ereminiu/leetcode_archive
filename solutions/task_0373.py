from heapq import*

class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        n, m = len(nums1), len(nums2)
        k = min(k, n*m)
        shift = n * [0]
        h = []
        for i in range(n):
            heappush(h, (nums1[i]+nums2[shift[i]], i))
        ans = []
        for rep in range(k):
            idx = heappop(h)[1]
            ans.append([nums1[idx], nums2[shift[idx]]])
            shift[idx] += 1
            if shift[idx] < m:
                heappush(h, (nums1[idx]+nums2[shift[idx]], idx))
        return ans