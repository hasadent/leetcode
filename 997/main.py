from typing import List
import time

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        N += 1
        tee = [0] * N
        ted = [0] * N
        for t in trust:
            tee[t[0]] += 1
            ted[t[1]] += 1
        
        i = 1
        while i < N:
            if tee[i] == 0 and ted[i] == (N - 2):
                return i
            i += 1
        return -1

def test(N, trust, ans):
    s = Solution()
    r = s.findJudge(N, trust)
    if r != ans:
        print('N=%d, trust=%s => %s, %s' % (N, trust, r, ans))


test(2, [[1,2]], 2)
test(3, [[1,3],[2,3]], 3)
test(3, [[1,3],[2,3],[3,1]], -1)
test(3, [[1,2],[2,3]], -1)
test(4, [[1,3],[1,4],[2,3],[2,4],[4,3]], 3)
test(1, [], 1)


