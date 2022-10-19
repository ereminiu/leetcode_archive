class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1); m = len(nums2)
        i = 0; j = 0
        a = []
        while i != n or j != m:
            if i == n:
                a.append(nums2[j])
                j += 1
                continue
            elif j == m:
                a.append(nums1[i])
                i += 1
                continue
            if nums1[i] <= nums2[j]:
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j += 1
        if (n+m) % 2:
            return float(a[(n+m)//2])
        return (a[(n+m)//2] + a[(n+m)//2-1]) / 2