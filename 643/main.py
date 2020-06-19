from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        m = s

        i = k
        while i < len(nums):
            s -= nums[i-4]
            s += nums[i]
            i += 1

            if s > m:
                m = s
        return m / k


def test(nums, k):
    s = Solution()
    r = s.findMaxAverage(nums, k)
    print(r)

test([1,12,-5,-6,50,3], 4)
