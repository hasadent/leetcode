from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        maxv = max(nums)
        minv = min(nums)
        bucket_size  = (maxv - minv + n - 2) // (n - 1)
        if bucket_size == 0:
            return 0

        bucket_num = (maxv - minv + bucket_size - 1) // bucket_size + 1
        buckets = [[4294967295, -1] for _ in range(n)]

        for n in nums:
            i = (n - minv) // bucket_size
            buckets[i][0] = min(buckets[i][0], n)
            buckets[i][1] = max(buckets[i][1], n)

        buckets = [b for b in buckets if b[1] != -1]
        r = 0
        for i in range(1, len(buckets)):
            r = max(r, buckets[i][0] - buckets[i-1][1])

        return r

def test(nums, ans):
    s = Solution()
    r = s.maximumGap(nums)
    if r != ans:
        print('x', nums, r, ans)

test([3,6,9,1], 3)
test([0], 0)
test([1,10000000], 10000000-1)
test([100,3,2,1], 97)
