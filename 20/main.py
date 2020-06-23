
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            v = ord(c) 
            if v == 40 or v == 91 or v == 123:
                stack.append(v)
                continue

            if len(stack) == 0 or (stack.pop() ^ v) > 6:
                return False
            
        return len(stack) == 0



def test(inp, ans):
    s = Solution()
    r = s.isValid(inp)
    if r != ans:
        print ('%s => %s, should be %s' % (inp, r, ans))


test('()',     True)
test('()[]{}', True)
test('(]',     False)
test('([)]',   False)
test('{[]}',   True)
