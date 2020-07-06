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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]
        while len(queue) != 0:
            next_lv_q = []
            cur = []

            for n in queue:
                cur.append(n.val)
                if n.left:
                    next_lv_q.append(n.left)
                if n.right:
                    next_lv_q.append(n.right)

            res.append(cur)
            queue = next_lv_q
        return res

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]
        while len(queue) != 0:
            next_lv_q = []
            cur = []

            for n in queue:
                cur.append(n.val)
                if n.left:
                    next_lv_q.append(n.left)
                if n.right:
                    next_lv_q.append(n.right)

            res.insert(0, cur)
            queue = next_lv_q
        return res


def test(root, ans):
    s = Solution()

    r = s.levelOrder(root)
    print('level   %s' % r)

    r = s.levelOrderBottom(root)
    print('level/b %s' % r)



root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
test(root, None)

test(None, None)

root = TreeNode(3, TreeNode(1), TreeNode(2))
test(root, None)


root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, TreeNode(5)))
test(root, None)

