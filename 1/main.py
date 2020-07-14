from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            n = target - nums[i]
            for j in range(i+1, l):
                if nums[j] == n:
                    return [i, j]
        return []


def test(nums, target, ans):
    s = Solution()
    r = s.twoSum(nums, target)
    if r != ans:
        print('not correct', nums, target, r, ans)

test([2, 7, 11, 15], 9, [0, 1])
test([0,4,3,0], 0, [0,3])
