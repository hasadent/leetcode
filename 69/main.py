import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        v = 0x8000
        r = 0
        while v != 0:
            a = r + v
            if a * a <= x:
                r = a
            v >>= 1
        return r


def test(x):
    s = Solution()

    r = s.mySqrt(x)
    rr = int(math.sqrt(x))

    if r != rr:
        print('sqrt of %d > %d %d' %  (x, r, rr))


test(4)
test(8)
test(9)
test(1024)
test(2048)
test(10000)
test(100000)
test(1000000)
for i in range(1, 100000):
    test(i)
