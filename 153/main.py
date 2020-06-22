from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
           return nums[0]

        s = len(nums)
        b = s - 1
        v = 0
        while nums[v] < nums[v+1]:
            r = (b - v) // 2
            if nums[v+r] > nums[v]:
                v = v + r
            else:
                b = v + r

        return nums[v+1]

def test(nums, ans):
    s = Solution()

    r = s.findMin(nums)

    if r != ans:
        print('%s => %d %d' % (nums, r, ans))

test([1], 1)
test([3,4,5], 3)
test([3,4,5,1,2], 1)
test([4,5,6,7,0,1,2], 0)
test([6,7,8,9,10,11,0,1,2,3,4,5], 0)
test([6,1,2,3,4,5], 1)
test([2,3,4,5,6,7,8,9,1], 1)
