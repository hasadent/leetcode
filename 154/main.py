from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = len(nums)
        if s == 1 or nums[0] < nums[-1]:
            return nums[0]

        b = s - 1
        v = 0
        while (v+1) < s and nums[v] <= nums[v+1]:
            r = (b - v) // 2

            if nums[v] < nums[v+r]:
                v = v + r
            elif nums[v] == nums[v+r]:
                v = v + 1
            elif nums[v+r] == nums[b]:
                b = b - 1
            else:
                b = v + r

        return nums[v+1] if (v+1) < s else nums[v]

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

test([2,2,2,0,1],0)
test([2,2,2,3,4,5,6,0,1],0)
test([3,1,3], 1)
test([1,1], 1)
test([1,1,1], 1)
test([1,1,1,1], 1)
