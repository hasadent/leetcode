from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        bound = len(matrix)

        for i in range(0, bound):
            for j in range(i+1,bound):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t

        for i in range(0, bound):
            for j in range(0, bound // 2):
                k = bound - j - 1
                t = matrix[i][j]
                matrix[i][j] = matrix[i][k]
                matrix[i][k] = t

def pp(matrix, title):
    print(title)
    for l in matrix:
        print(l)

def test(matrix, answer):
    s = Solution()
    s.rotate(matrix)

    if matrix != answer:
        pp(matrix, 'mine')
        pp(matrix, 'answer')


a = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
];

b = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

test(a, b)

a = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

b = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

test(a, b)
