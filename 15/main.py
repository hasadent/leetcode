from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(start, target):
            p = {}
            r = []

            for i in range(start, len(nums)):
                n = nums[i]
                d = target - n
                if d in p:
                    r.append((p[d], i))
                p[n] = i
            return r

        nums.sort()
        h = {}
        r = []
        for i in range(0, len(nums) - 2):
            n = nums[i]
            if i != 0 and n == nums[i - 1]:
                continue

            res = twoSum(i + 1, -n)
            for x, y in res:
                item = [n, nums[x], nums[y]]

                if not tuple(item) in h:
                    h[tuple(item)] = True
                    r.append(item)

        return r


def test(nums, ans):
    s = Solution()
    r = s.threeSum(nums)
    if r != ans:
        print('not correct', nums, r, ans)

test([-1, 0, 1, 2, -1, -4], [[-1, 0, 1],[-1, -1, 2]])
test([-2,0,1,1,2], [[-2,0,2],[-2,1,1]])
