import math

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        lcm = A * B // math.gcd(A, B)
        cnt = lcm // A + lcm // B - 1

        x = ((N // cnt) * lcm) % 1000000007
        y = N % cnt
        if y == 0:
            return x

        l, r = 0, lcm - 1 
        while l < r:
            m = (l + r) // 2
            v = m // A + m // B
            if v >= y:
                r = m
            else:
                l = m + 1

        return (l+x) % 1000000007


def test(N, A, B, ans):
    s = Solution()
    r = s.nthMagicalNumber(N, A, B)
    if r != ans:
        print('not correct', N, A, B, r, ans)

test(1, 2, 3, 2)
test(4, 2, 3, 6)
test(5, 2, 4, 10)
test(3, 6, 4, 8)

            

