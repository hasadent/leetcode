class Solution:
    tbl = (0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4)

    def hammingWeight(self, n: int) -> int:
        s = 0
        while n != 0:
            s += self.tbl[n & 0xf]
            n >>= 4
        return s


def test(n, ans):
    s = Solution()
    r = s.hammingWeight(n)

    if r != ans:
        print('%d -> %x: %d %d' % (n, n, r, ans))
            


test(0, 0)

test(1, 1)
test(2, 1)
test(3, 2)
test(4, 1)
test(5, 2)
test(6, 2)
test(7, 3)
test(8, 1)
test(9, 2)
test(10, 2)
test(11, 3)
test(12, 2)
test(13, 3)
test(14, 3)
test(15, 4)

test(16, 1)
test(32, 1)


test(255, 8)
test(65535, 16)
