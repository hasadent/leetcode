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
            s += ' ' + str(self.right)
        return s


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        if not root:
            return res

        stack = [root]
        while len(stack) != 0:
            n = stack.pop()

            res.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

        return res


    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        if not root:
            return res

        stack = [root]
        while len(stack) != 0:
            n = stack.pop()

            res.insert(0, n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

        return res


def test(root, ans):
    s = Solution()

    r = s.preorderTraversal(root)
    print('pre %s' % r)

    r = s.postorderTraversal(root)
    print('post %s' % r)


root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
test(root, None)

test(None, None)

root = TreeNode(3, TreeNode(1), TreeNode(2))
test(root, None)



