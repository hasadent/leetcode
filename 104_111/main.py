import sys
sys.path.append('../common')

from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        lv = 0
        q, nq = [root], []
        while q:
            n = q.pop(0)
            if n.left:
                nq.append(n.left)
            if n.right:
                nq.append(n.right)
            if len(q) == 0:
                q, nq = nq, []
                lv += 1
        return lv

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        lv = 0
        q, nq = [root], []
        while q:
            n = q.pop(0)
            if not n.left and not n.right:
                return lv + 1

            if n.left:
                nq.append(n.left)
            if n.right:
                nq.append(n.right)
            if len(q) == 0:
                q, nq = nq, []
                lv += 1
        return lv


def test(treeList, ans_0, ans_1):

    root = TreeNode.fromList(treeList)

    s = Solution()
    r = s.maxDepth(root)
    ans = ans_0

    if r != ans:
        print('maxDepth: not correct', 'output:', r, 'excpeted:', ans)
        root.printTree()

    r = s.minDepth(root)
    ans = ans_1
    if r != ans:
        print('minDepth: not correct', 'output:', r, 'excpeted:', ans)
        root.printTree()

test([3,9,20,None,None,15,7], 3, 2)
test([1,2], 2, 2)
