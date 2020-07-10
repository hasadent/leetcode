from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s, d = set(), set()
        for p in paths:
            s.add(p[0])
            d.add(p[1])
        return (d - s).pop()
        

def test(paths, ans):
    s = Solution()
    r = s.destCity(paths)
    if r != ans:
        print('not correct', 'paths', paths, 'mine', r, 'answer', ans)

test([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], "Sao Paulo")



