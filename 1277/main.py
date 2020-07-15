from typing import List

class Solution:
    def countSquares_1(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        q = [ (x, y) for x in range(n) for y in range(m) if matrix[x][y] == 1 ]
        s = len(q)

        for i in range(1, min(n, m)):
            next_q = []
            for x, y in q:
                if (x+i) >= n or (y+i) >= m:
                    continue

                not_square = False
                for j in range(i+1):
                    if matrix[x+i][y+j] == 0 or matrix[x+j][y+i] == 0:
                        not_square = True
                        break
                if not_square:
                    continue
                s += 1
                next_q.append((x, y))

            q = next_q
            if len(q) == 0:
                break

        return s

    def countSquares(self, matrix: List[List[int]]) -> int:
        s = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue

                if i > 0 and j > 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                s += matrix[i][j]
        return s




def test(matrix, ans):
    s = Solution()
    r = s.countSquares(matrix)
    if r != ans:
        print('not correct', matrix, r, ans)

test([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
], 15)


test([
  [1,0,1],
  [1,1,0],
  [1,1,0]
], 7)

test([
    [0,0,0],
    [0,1,0],
    [0,1,0],
    [1,1,1],
    [1,1,0]
], 8)

