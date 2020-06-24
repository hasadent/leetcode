from typing import  List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = str(self.val)
        if self.left:
            s += ' ' + str(self.left)
        if self.right:
            s += ' r:' + str(self.right)
        return s


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        cur = root
        stack = [root]
        while len(stack) != 0:

            n = stack.pop()

            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
                n.left = None

            cur.right = n
            cur = n

        cur.right = None



def test(root):
    s = Solution()

    r = s.flatten(root)
    print('flatten: %s' % root)


root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
test(root)

test(None)

root = TreeNode(3, TreeNode(1), TreeNode(2))
test(root)


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
test(root)

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
test(root)

test(TreeNode())
