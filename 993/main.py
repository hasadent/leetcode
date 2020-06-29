
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [root]
        queue_next = []
        found = 0
        lv = 0
        while len(queue) != 0:
            n = queue.pop(0)
            if n.left:
                if n.left.val == x:
                    xp, xlv = n, lv
                    found += 1
                elif n.left.val == y:
                    yp, ylv = n, lv
                    found += 1
                else:
                    queue_next.append(n.left)
            if n.right:
                if n.right.val == x:
                    xp, xlv = n, lv
                    found += 1
                elif n.right.val == y:
                    yp, ylv = n, lv
                    found += 1
                else:
                    queue_next.append(n.right)

            if found == 2:
                return xlv == ylv and xp != yp

            if len(queue) == 0:
                if found == 1:
                    return False
                lv += 1
                queue = queue_next
                queue_next = []

        return False


def test(root, x, y, ans):
    s = Solution()
    r = s.isCousins(root, x, y)

    if r != ans:
        print('%d %d => %s %s' % (x, y, r, ans))


test(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 4, 3, False)
test(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5))), 5, 4, True)
test(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), 2, 3, False)
