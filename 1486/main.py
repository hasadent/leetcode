import time

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [i for i in range(start + 2, start+n*2, 2)]

        r = start
        for x in nums:
            r = r^x
        return r


    def refXorOperation(self, n: int, start: int) -> int:
        nums = [start + i*2 for i in range(0, n)]

        r = 0
        for x in nums:
            r = r^x
        return r


def test(n, start):
    s = Solution()
    max_run = 10000

    start_time = time.time()
    for i in range(1, max_run):
        r = s.xorOperation(n, start)
    print("alg0 --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for i in range(1, max_run):
        rr = s.refXorOperation(n, start)
    print("alg1 --- %s seconds ---" % (time.time() - start_time))

    if r != rr:
        print('n=%d, start=%d => %d %d' %(n, start, r, rr))

test(5,0)
test(4,3)
test(100,3)


