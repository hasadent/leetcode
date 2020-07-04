from typing import List

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and stack[-1][1] >= h:
                _, ch = stack.pop()
                cw = i - stack[-1][0] - 1 if stack else i
                max_area = max(max_area, cw * ch)
            stack.append((i, h))

        return max_area

def test(heights, ans):
    s = Solution()
    r = s.largestRectangleArea(heights)
    if r != ans:
        print('x', heights, r, ans)


test([2,1,5,6,2,3], 10)
test([0,0,0,0,0,0,0,0,2147483647], 2147483647)

test([2,1,5,6,1,3], 10)
