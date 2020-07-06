from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def getEquivalent(v, name):
            while True:
                r = v[name]
                if r == name:
                    return r
                name = r
        v = {}
        equations_ne = []
        for eq in equations:
            if eq[1] != '=':
                equations_ne.append(eq)
                continue

            v0 = eq[0]
            v1 = eq[3]
            if not v0 in v:
                v[v0] = v0
            if not v1 in v:
                v[v1] = getEquivalent(v, v0)
                continue

            new = getEquivalent(v,v0)
            old = getEquivalent(v,v1)
            if old != new:
                for k in v.keys():
                    if v[k] == old:
                        v[k] = new

        for eq in equations_ne:
            v0 = eq[0]
            v1 = eq[3]
            if not v0 in v:
                v[v0] = v0
            if not v1 in v:
                v[v1] = v1
                continue

            eval_eq = getEquivalent(v, v0) != getEquivalent(v,v1)
            if not eval_eq:
                return False

        return True



def test(equations, ans):
    s = Solution()
    r = s.equationsPossible(equations)
    if r != ans:
        print('incorrect', equations, r, ans)

test(["a==b","b!=a"], False)
test(["b==a","a==b"], True)
test(["a==b","b==c","a==c"], True)
test(["a==b","b!=c","c==a"], False)
test(["c==c","b==d","x!=z"], True)
test(["c==c","f!=a","f==b","b==c"],True)


test(["f==a","a==b","f!=e","a==c","b==e","c==f"], False)
test(["b==b","b==e","e==c","d!=e"],True)
