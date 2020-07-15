from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        while l < r:

            if height[l] >= height[r]:
                area_new = height[r] * (r - l)
                r -= 1
            else:
                area_new = height[l] * (r - l)
                l += 1
            area = max(area_new, area)
        return area


def test(height, ans):
    s = Solution()
    r = s.maxArea(height)
    if r != ans:
        print('not correct', height, r, ans)

test([1,8,6,2,5,4,8,3,7], 49)
        
