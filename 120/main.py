from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, i + 1):
                triangle[i][j] += min( triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

def test(triangle, ans):
    s = Solution()
    r = s.minimumTotal(triangle)
    if r != ans:
        print('not correct', r, ans)
        print('triangle', triangle)


test([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
], 11)
test([[-1],[3,2],[-3,1,-1]], -1)
