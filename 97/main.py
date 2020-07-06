class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)

        if ls3 != (ls1 + ls2):
            return False
        if ls3 == 0:
            return True

        ls1 += 1
        ls2 += 1

        dp = [ [0] * (ls1) for _ in range(ls2) ]
        dp[0][0] = 1

        for i in range(1, ls1):
            if s1[i - 1] == s3[i - 1] and dp[0][i - 1] == 1:
                dp[0][i] = 1
            else:
                break

        for j in range(1, ls2):
            if s2[j - 1] == s3[j - 1] and dp[j - 1][0] == 1:
                dp[j][0] = 1
            else:
                break

        for j in range(1, ls2):
            for i in range(1, ls1):
                c1, c2, c3 = s1[i - 1], s2[j - 1], s3[i + j - 1]

                if c1 != c2:
                    if c1 == c3:
                        dp[j][i] = dp[j][i - 1]

                    elif c2 == c3:
                        dp[j][i] = dp[j - 1][i]

                elif c1 == c3:
                     dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

        return dp[-1][-1] != 0


def test(s1, s2, s3, ans):
    s = Solution()
    r = s.isInterleave(s1, s2, s3)
    if r != ans:
        print(s1, s2, s3, r, ans)

test("aabcc", "dbbca", "aadbbcbcac", True)
test("aabcc", "dbbca", "aadbbbaccc", False)
test("a", "b", "a", False)
test("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab",
False)

test("a", "b", "ab", True)
test("", "", "", True)
