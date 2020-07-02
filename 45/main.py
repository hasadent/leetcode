from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0:
            return 0

        for i in range(0, n):
            nums[i] += i

        r = 1
        i = 0
        while nums[i] < n:
            for j in range(i + 1, nums[i] + 1):
                if nums[i] <= nums[j]:
                    i = j
            r += 1
        return r


def test(nums, ans):
    s = Solution()
    r = s.jump(nums)
    if r != ans:
        print('x', nums, r, ans)


test([2,3,1,1,4], 2)
test([1,1], 1)
test([0], 0)
test([1,2,3], 2)
test([8,4,3,4,0,0,9,7,2,3,5,7,3,1,1,5,1,8,6,1,1,6,1,1,8,0,4], 5)
