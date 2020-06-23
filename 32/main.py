class Solution:
    ''' stack '''
    def _longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
                continue

            p = stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                longest = max(longest, i - stack[-1])

        return longest

    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, left+right)
            elif right > left:
                left = right = 0

        left = right = 0
        for c in reversed(s):
            if c == '(':
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, left+right)
            elif right < left:
                left = right = 0
        return longest


def test(inp, l):
    s = Solution()

    r = s.longestValidParentheses(inp)

    if r != l:
        print('%s -> %d %d' % (inp, r, l))


test('(((()', 2)
test('()))', 2)
test('(()', 2)
test('', 0)
test(')()())', 4)
test(')(((()))', 6)
test(')(((()(())))', 10)
test('()(()', 2)
test('(())(()', 4)

test('()(((()()))(()()()', 8)
test('())((()())))()()()', 8)

test(')()())', 4)
test(')', 0)
test(')(', 0)
test('(', 0)
test('()()', 4)
test('((()))())', 8)
test(')()(((())))(', 10)
