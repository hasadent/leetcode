class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(-1)
            else:
                v = 0
                while stack[-1] != -1:
                    v += stack.pop()

                stack.pop()
                stack.append(max(1, v*2))

        return sum(stack)


def test(S, ans):
    s = Solution()
    r = s.scoreOfParentheses(S)
    if r != ans:
        print('not correcnt', 'S', S, 'mine',  r, 'answer', ans)


test("()", 1)
test("(())", 2)
test("()()", 2)
test("(()(()))", 6)


