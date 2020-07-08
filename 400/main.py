t = [(9, 0), (189, 9), (2889, 108), (38889, 1107), (488889, 11106), (5888889, 111105), (68888889, 1111104), (788888889, 11111103), (8888888889, 111111102)]

class Solution:
    def findNthDigit(self, n: int) -> int:
        global t

        if n < 10:
            return n

        for i, x in enumerate(t):
            if n <= x[0]:
                break
        n += x[1] + i

        div = i + 1
        v = n // div
        i = n % div
        return ord(str(v)[i]) - 48

def test(n, ans):
    s = Solution()
    r = s.findNthDigit(n)
    if r != ans:
        print('not correct', n, r, ans)



# 3
test(3, 3)

# 10
test(10, 1)
test(11, 0)

# 11
test(12, 1)
test(13, 1)

# 99
test(188, 9)
test(189, 9)


# 999
test(2887, 9)
test(2888, 9)
test(2889, 9)
