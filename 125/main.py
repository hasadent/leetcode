class Solution:
    def isPalindrome(self, s: str) -> bool:
        def func(v):
            if 97 <= v and v <= 122:
                return v
            if 65 <= v and v <= 90:
                return v | 32
            if 48 <= v and v <= 57:
                return v
            return 0

        l, r = 0, len(s) - 1
        while l < r:
            h = func(ord(s[l]))
            t = func(ord(s[r]))

            if h == 0:
                l += 1
                continue
            if t == 0:
                r -= 1
                continue

            if h != t:
                return False
            l += 1
            r -= 1
        return True


def test(s, ans):
   r = Solution().isPalindrome(s)
   if r != ans:
       print('*** not correct ***')
       print('\tinput=', s)
       print('\tresult=', r)
       print('\tanswer=', ans)


test("A man, a plan, a canal: Panama", True)
test("race a car", False)

test("", True)
test(".", True)

test("0P", False)
test("ab_a", True)
