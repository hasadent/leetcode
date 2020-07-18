from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        v = {}
        for s in emails:
            x = s.split('@')
            if len(x) != 2:
                continue

            plus = x[0].find('+')
            if plus > 0:
                x[0] = x[0][0:plus]

            x[0] = x[0].replace('.','')

            v[x[0] + '@' + x[1]] = True
        return len(v.keys())





def test(emails, ans):
    r = Solution().numUniqueEmails(emails)
    if r != ans:
        print('not correct', '\n\tinput=', emails, '\n\tresult=', r, ans)



test(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"], 2)


        
