class Solution:
    def countSubstrings(self, s: str) -> int:
        count = l = len(s)
        if l == 0:
            return 0

        for i in range(l):

            a, b = i, i + 1
            while a >= 0 and b < l and s[a] == s[b]:
                count += 1
                a -= 1
                b += 1

            a, b = i - 1, i + 1
            while a >= 0 and b < l and s[a] == s[b]:
                count += 1
                a -= 1
                b += 1

        return count


def test(inp, ans):
    s = Solution()
    r = s.countSubstrings(inp)
    if r != ans:
        print('x', inp, r, ans)

test('abc', 3)
test('aaa', 6)
test('', 0)
test('aabaa', 9)
