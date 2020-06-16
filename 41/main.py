from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        i = 1
        l = 0
        for n in nums:
            if l == n:
                continue
            l = n
            if n <= 0:
                continue

            if n != i:
                break
            i+=1
            m = n

        return i

def test(l):
    s = Solution()
    r = s.firstMissingPositive(l)
    print ('%s => %s' % (l, r))


test([1,2,0])
test([3,4,-1,1])
test([7,8,9,11,12])
test([1,1])
test([0,2,2,1,1])
