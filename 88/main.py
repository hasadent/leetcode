from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = n, 0, 0
        nums1[-m:] = nums1[0:m]

        while i < (m+n) and j < n:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if j < n:
            nums1[j-n:] = nums2[j:]



s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge(nums1, 3, nums2, 3)
print(nums1)
