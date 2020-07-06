from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        i = 1
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            i += 1
        return target in matrix[i-1]



def test(matrix, target, ans):
    s = Solution()
    r = s.searchMatrix(matrix, target)

    if r != ans:
        print(matrix, target, r, ans)


test([
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 3, True)

test([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13, False)

test([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 50, True)


test([], 0, False)
