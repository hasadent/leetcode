from typing import List

class Solution:
    a = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solveSudoku(self, board: List[List[str]]) -> None:
        x = [set() for _ in range(9)]
        y = [set() for _ in range(9)]
        z = [set() for _ in range(9)]

        def backtrack(i, j):
            if i >= 9:
                return True

            if j >= 9:
                return backtrack(i+1, 0)

            if board[i][j] != '.':
                return backtrack(i, j+1)

            k = (i // 3) * 3 + (j // 3)

            unused = (x[i] | y[j] | z[k]) ^ self.a
            for u in unused:
                board[i][j] = u
                x[i].add(u)
                y[j].add(u)
                z[k].add(u)

                if backtrack(i, j+1):
                    return True

                board[i][j] = '.'
                x[i].remove(u)
                y[j].remove(u)
                z[k].remove(u)

            return False

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    continue

                x[i].add(v)
                y[j].add(v)
                z[(i // 3) * 3 + (j // 3)].add(v)

        return backtrack(0, 0)


def test(board, ans):
    s = Solution()
    s.solveSudoku(board)

    if board != ans:
        for i in range(len(board)):
            print(board[i], ' ', ans[i])

test(
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
)
test(
[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]],
[["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
)
