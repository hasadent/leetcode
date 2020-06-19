from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = [0, 0, 0]
        for n in nums:
            c[n] += 1

        i = 0
        j = 0
        while j < 3:
            k = 0
            while k < c[j]:
                nums[i] = j
                i+=1
                k+=1
            j += 1


def test(l):

    rr = sorted(l)

    s = Solution()
    s.sortColors(l)


    if l != rr:
        print('my %s, sort %s' %(l, rr))

test([2,0,2,1,1,0])
test([0,0,1,0,2,0,2])







