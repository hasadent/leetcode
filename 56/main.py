from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort()
        r = []
        x = intervals[0]

        for y in intervals:
            if y[0] <= x[1]:
                x[1] = max(x[1], y[1])
            else:
                r.append(x)
                x = y
        if x:
            r.append(x)
        return r
            


def test(intervals, ans):
    s = Solution()
    r = s.merge(intervals.copy())
    if r != ans:
        print('not correct', intervals, r, ans)



test([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]])
test([[1,4],[4,5]], [[1,5]])
test([[1,3]], [[1,3]])
test([], [])
test([[1,4],[0,4]], [[0,4]])
test([[1,4],[0,0]], [[0,0], [1,4]])
