class Solution:
    def intToRoman(self, num: int) -> str:
        out = []
        while num >= 1000:
            out.append('M')
            num -= 1000

        if num >= 900:
            out.append('CM')
            num -= 900

        if num >= 500:
            out.append('D')
            num -= 500

        if num >= 400:
            out.append('CD')
            num -= 400

        while num >= 100:
            out.append('C')
            num -= 100

        if num >= 90:
            out.append('XC')
            num -= 90

        if num >= 50:
            out.append('L')
            num -= 50

        if num >= 40:
            out.append('XL')
            num -= 40

        while num >= 10:
            out.append('X')
            num -= 10

        if num >= 9:
            out.append('IX')
            num -= 9

        if num >= 5:
            out.append('V')
            num -= 5

        if num >= 4:
            out.append('IV')
            num -= 4

        out.append('I' * num)

        return ''.join(out)


    def romanToInt(self, s: str) -> int:
        o = 0
        i = 0

        # since position i+1 maybe be checked in some caese, append
        # an extra charactor to avoid boundary checking
        s += '.'
        b = len(s)
        while i < b:
            if s[i] == 'M':
                o += 1000
                i += 1
            elif s[i] == 'D':
                o += 500
                i += 1
            elif s[i] == 'C':
                if s[i+1] == 'M':
                    o += 900
                    i += 2
                elif s[i+1] == 'D':
                    o += 400
                    i += 2
                else:
                    o += 100
                    i += 1
            elif s[i] == 'L':
                o += 50
                i += 1
            elif s[i] == 'X':
                if s[i+1] == 'C':
                    o += 90
                    i += 2
                elif s[i+1] == 'L':
                    o += 40
                    i += 2
                else:
                    o += 10
                    i += 1
            elif s[i] == 'V':
                o += 5
                i += 1
            elif s[i] == 'I':
                if s[i+1] == 'X':
                    o += 9
                    i += 2
                elif s[i+1] == 'V':
                    o += 4
                    i += 2
                else:
                    o += 1
                    i += 1
            else:
                i += 1

        return o


def test(num):
    s = Solution()
    r0 = s.intToRoman(num)
    r1 = s.romanToInt(r0)

    if num != r1:
        print('%d -> %s -> %d' % (num, r0, r1))

cases = range(1, 4000)
for c in cases:
    test(c)

