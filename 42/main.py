from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        ret = 0

        i = 1
        pi, pv = 0, height[0]
        while i < len(height):
            if height[i] > pv:
                pi, pv = i, height[i]
            else:
                npi, npv = i, height[i]
                for j in range(i + 1, len(height)):
                    if height[j] > npv:
                        npi, npv = j, height[j]
                    if height[j] > pv:
                        break

                if (pi + 1) != npi:
                    h = min(pv, npv)
                    for j in range(pi + 1, npi):
                        if height[j] < h:
                             ret += h - height[j]

                pi, pv = npi, npv
                i = npi
            i += 1

        return ret

def test(height, ans):
    s = Solution()

    r = s.trap(height)
    if r != ans:
        print(height, r, ans)


test([0,1,0,2,1,0,1,3,2,1,2,1], 6)
test([5,4,1,2], 1)
test([5,2,1,2,1,5], 14)
