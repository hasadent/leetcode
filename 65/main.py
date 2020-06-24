
class Solution:
    def isNumber(self, s: str) -> bool:

        def isInt(s):
            if s == '':
                return False

            if s[0] == '+' or s[0] == '-':
                s = s[1:]

            return s.isdigit()

        def isFloat(s):
            if s == '':
                return False

            if s[0] == '+' or s[0] == '-':
                s = s[1:]

            if s == '.':
                return False

            ss = s.split('.', 1)

            r = ss[0].isdigit()
            if len(ss) == 1:
               return r
            return (r or ss[0] == '') and (ss[1] == '' or ss[1].isdigit())

        ss = s.lstrip().rstrip().split('e', 1)

        r = isFloat(ss[0])
        if len(ss) == 1:
            return r
        return r and isInt(ss[1])


def test(ss, ans):
    s = Solution()

    r = s.isNumber(ss)
    if r != ans:
        print('incorrect:: %s => %s %s' %(ss, r, ans))


test("0", True)
test(" 0.1 ", True)
test("abc", False)
test("1 a", False)
test("2e10", True)
test(" -90e3   ", True)
test(" 1e", False)
test("e3", False)
test(" 6e-1", True)
test(" 99e2.5 ", False)
test("53.5e93", True)
test(" --6 ", False)
test("-+3", False)
test("95a54e53", False)
test('1e2e3', False)
test('-1.e3', True)
test('-1.', True)
test('1.i.', False)
test('i.1', False)
test('.1', True)
test('.1e', False)
test('.1e1', True)
test('.e1', False)
test('.', False)
test('-e58', False)

