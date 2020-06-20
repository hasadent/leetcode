
class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        if x < 0:
            x = -x
            r = 1

        y = int(str(x)[::-1])

        if r:
            y = -y

        if y < -0x80000000 or y > 0x7fffffff:
            return 0
        return y


def test(x, y):
    s = Solution()

    r = s.reverse(x)

    if r != y:
        print('%d %d' % (r, y))

test(123, 321)
test(-123, -321)
test(210, 12)
test(1534236469, 0)
test(-2147483412, -2143847412)

