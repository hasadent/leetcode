from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        cur = nums[0]

        for i in range(length):
            if cur >= length - 1:
                return True
            if i > cur:
                return False
            cur = max(cur, i + nums[i])


def test(nums, ans):
    s = Solution()
    r = s.canJump(nums.copy())
    if r != ans:
        print('not correct', nums, r, ans)

test([2,3,1,1,4], True)
test([3,2,1,0,4], False)
test([1,2,3],   True)
test([0], True)
test([0, 1], False)
