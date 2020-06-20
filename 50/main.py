import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        r = 1
        while n > 0:
            while (n % 2) == 0:
                x *= x
                n = n // 2
            r *= x
            n -= 1
        return r


def __pow(x, n):
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    r = 1
    while n > 0:
        r *= x
        n -= 1
    return r




def test(x, n):
    s = Solution()
    r = s.myPow(x, n)
    rr = __pow(x, n)
    print('%f^%d => my %f pow %f' % (x, n, r, rr))
    if r != rr:
        print('not equal')


test(2.00000, 10)
test(2.10000, 3)
test(2.00000, -2)
test(2.00000, 513)

test(2.00000, 1023)
test(2.00000, 1024)

