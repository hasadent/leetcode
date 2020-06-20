import math

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        r = m & n
        if r == 0:
            return 0

        d = n - m
        if d == 0:
            return r

        y = int(math.log2(d)) + 1
        r = r & ~((1 << y) - 1)
        return r

def calc(m, n):
    i = m + 1
    r = m
    while i <= n:
        r = r & i
        i += 1
    return r


def test(m, n):
    s = Solution()
    r = s.rangeBitwiseAnd(m, n)
    rr = calc(m, n)
    if r != rr:
        print('(%d-%d) => %d, %d' % (m, n, r, rr))

test(5, 7)
test(0, 1)
test(10, 20)
test(11, 20)
test(9, 10)
test(21, 29)
test(22, 29)
for y in range(22,32):
    test(22, y)
test(32, 63)
test(33, 63+64)
