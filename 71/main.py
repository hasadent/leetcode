class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split('/')
        stack = ['']
        for s in sp:
            if s == '' or s == '.':
                continue
            elif s == '..':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(s)

        if len(stack) == 1:
            return '/'
        return '/'.join(stack)


def test(path, ans):
    s = Solution()
    r = s.simplifyPath(path)
    if r != ans:
        print(path, 'mine', r, 'answer', ans)


test('/home/', '/home')
test('/../', '/')
test('/home//foo/', '/home/foo')
test('/a/./b/../../c/', '/c')
test('/a/../../b/../c//.//', '/c')
test('/a//b////c/d//././/..', '/a/b/c')

