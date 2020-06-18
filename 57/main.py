from typing import List

def overlap(i_0, i_1):
    return max(i_0[0], i_1[0]) <= min(i_0[1], i_1[1])

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            if not overlap(intervals[i], newInterval):
                i += 1
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            del intervals[i]
        intervals.insert(i, newInterval)
        return intervals

'''
# test overlap
print(overlap([1,2], [2,3]))
print(overlap([2,5], [1,3]))
print(overlap([1,3], [2,3]))
print(overlap([4,8], [8,10]))
print(overlap([4,7], [8,10]))
'''



def test(intervals, newInterval, answer):

    print('input: intervals = %s, newInterval = %s' % (intervals, newInterval))
    s = Solution()
    r = s.insert(intervals, newInterval)

    if r != answer:
        print('fail: mine = %s, answer = %s' % (r, answer))
    else:
        print('pass')

test([[1, 3], [6, 9]],                            [2, 5], [[1, 5], [6, 9]] )
test([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
test([[1, 5], [6, 9], [11, 14], [14, 16]],        [5, 7], [[1, 9], [11, 14], [14, 16]])
test([[1, 5]],                                    [2, 3], [[1, 5]])
test([],                                          [5, 7], [[5, 7]])
test([[1, 5]],                                    [0, 0], [[0, 0], [1, 5]])
test([[3, 5], [12, 15]],                          [6, 6], [[3, 5], [6, 6], [12, 15]])
test([[1, 5], [10, 11], [15, 2147483647]],        [5, 7], [[1, 7], [10, 11], [15, 2147483647]])
test([[1, 5], [6, 7]],                            [8, 9], [[1, 5], [6, 7], [8, 9]])
