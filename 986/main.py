from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a, b = len(A), len(B)
        if a == 0 or b == 0:
            return []

        r = []
        i = j = 0
        while i < a and j < b:
            if A[i][1] >= B[j][0] and A[i][0] <= B[j][1]:
                x = max(A[i][0], B[j][0])
                y = min(A[i][1], B[j][1])
                r.append([x,y])

            if A[i][1] == B[j][1]:
                i += 1
                j += 1
            
            elif A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return r

            


def test(A, B, ans):
    s = Solution()
    r = s.intervalIntersection(A.copy(), B.copy())
    if r != ans:
        print('not correct', '\n\tA=', A, '\n\tB=', B, '\n\tr=', r, '\n\ta=', ans)


test(
[[0,2],[5,10],[13,23],[24,25]],
[[1,5],[8,12],[15,24],[25,26]],
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
)

test(
[[8,15]],
[[2,6],[8,10],[12,20]],
[[8,10],[12,15]]
)

test(
[[3,5],[9,20]],
[[4,5],[7,10],[11,12],[14,15],[16,20]],
[[4,5],[9,10],[11,12],[14,15],[16,20]]
)
