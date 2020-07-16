from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        a, b, c, d = 1, 0, len(matrix), len(matrix[0])
        r = matrix[0].copy()
        i = 1
        while a < c and b < d:
            sel = i % 4
            if sel == 0:
                r.extend([matrix[a][j] for j in range(b, d)])
                a += 1
            elif sel == 1:
                r.extend([matrix[j][d-1] for j in range(a, c)])
                d -= 1
            elif sel == 2:
                r.extend([matrix[c-1][j] for j in range(d - 1, b - 1, -1)])
                c -= 1
            else:
                r.extend([matrix[j][b] for j in range(c - 1, a - 1, -1)])
                b += 1
            i += 1
        return r


def test(matrix, ans):
    s = Solution()
    r = s.spiralOrder(matrix)

    if r != ans:
        print('not correct', matrix, r, ans)

test([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
], [1,2,3,6,9,8,7,4,5])

test([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
], [1,2,3,4,8,12,11,10,9,5,6,7])

