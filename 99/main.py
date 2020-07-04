import sys
sys.path.append('../common')
from TreeNode import TreeNode

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        inv = []
        stack = []
        prev, curr = None, root
        while len(stack) != 0 or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev and prev.val > curr.val:
                inv.append((prev, curr))

            prev, curr = curr, curr.right

        inv[0][0].val, inv[-1][1].val = inv[-1][1].val, inv[0][0].val


def test(inpList, ansList):
    root = TreeNode.fromList(inpList)
    ans = TreeNode.fromList(ansList)

    s = Solution()
    s.recoverTree(root)
    if root != ans:
        print('mine')
        root.printTree()
        print('answer')
        ans.printTree()

test([1,3,None,None,2], [3,1,None,None,2])
test([3,1,4,None,None,2], [2,1,4,None,None,3])
