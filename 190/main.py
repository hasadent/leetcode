
tbl = (0x0, 0x8, 0x4, 0xC, 0x2, 0xA, 0x6, 0xE, 0x1, 0x9, 0x5, 0xD, 0x3, 0xB, 0x7, 0xF)

class Solution:
    def reverseBits(self, n: int) -> int:
        global tbl

        x = 0
        for i in range(0, 32, 4):
            x = (x << 4) +  tbl[(n >> i) & 0xf]
        return x



def test(n, ans):
    s = Solution()
    r = s.reverseBits(n)

    if r != ans:
        print('not correct', n, r, ans)


test(43261596, 964176192)
test(4294967293, 3221225471)

