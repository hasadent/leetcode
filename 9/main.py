import time

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 10000000:
            if x >= 1000000000:
                c, div = 5, 1000000000
            elif x >= 100000000:
                c, div = 4, 100000000
            else:
                c, div = 4, 10000000
        elif x >= 1000:
            if x >= 1000000:
                c, div = 3, 1000000
            elif x >= 100000:
                c, div = 3, 100000
            elif x >= 10000:
                c, div = 2, 10000
            else:
                c, div = 2, 1000
        elif x >= 100:
            c, div = 1, 100
        else:
            if x < 10:
                if x < 0:
                    return False
                return True
            c, div = 1, 10

        while c > 0 and x != 0:
            if (x // div) != (x % 10):
                return False
            x %= div
            x //= 10
            div //= 100
            c -= 1

        return True

    def isPalindrome_(self, x: int) -> bool:
        if x < 0:
            return False

        s0 = str(x)
        return s0[::-1] == s0

def test(x):
    max_run = 100000
    print('input=%d' % x)

    s = Solution()

    start_time = time.time()
    for i in range(1, max_run):
        r = s.isPalindrome(x)
    print("div --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for i in range(1, max_run):
        rr = s.isPalindrome_(x)
    print("str --- %s seconds ---" % (time.time() - start_time))

    if r != rr:
        print('%d => %s %s' % (x, r, rr))

test(123)
test(1)
test(121)
test(-121)
test(10)
test(1221)
test(11211)
test(1000021)
test(1000001)
