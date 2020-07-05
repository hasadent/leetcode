from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.toList())

    def __eq__(self, other):
        if not other or type(other) != TreeNode:
            return False

        return self.val == other.val and \
            self.left == other.left and \
            self.right == other.right

    def toList(self) -> List:
        root = self
        if not root:
            return []

        res, queue = [root.val], [root]
        while queue:
            n = queue.pop(0)

            lv = rv = None

            if n.left:
                queue.append(n.left)
                lv = n.left.val

            if n.right:
                queue.append(n.right)
                rv = n.right.val

            res.append(lv)
            res.append(rv)

        while res and res[-1] == None:
            res.pop()

        return res

    @staticmethod
    def fromList(data):
        if len(data) == 0:
            return None

        root, i = TreeNode(data[0]), 1
        queue = [root]
        while i < len(data):
            n = queue.pop(0)

            v, i = data[i], i + 1
            if v != None:
                n.left = TreeNode(v)
                queue.append(n.left)

            if i < len(data):
                v, i = data[i], i + 1
                if v != None:
                    n.right = TreeNode(v)
                    queue.append(n.right)

        return root

    def printTree(self, ident: int = 0):
        queue = [ (ident, self) ]

        while queue:
            ident, n = queue.pop()

            s = ' ' * ident
            if id(n) == id(self):
                s += 'Tree: %3d' % n.val
                ident += 9
            else:
                s += ' `-> %3d' % n.val
                ident += 8

            if n.right:
                queue.append((ident, n.right))

            nn = n.left
            while nn:
                s += ' --> %3d' % nn.val
                ident += 8
                if nn.right:
                    queue.append((ident, nn.right))
                nn = nn.left

            print(s)

if __name__ == '__main__':
    tree = TreeNode.fromList([3,9,20,None,None,15,7])
    tree.printTree()

    tree = TreeNode.fromList([1, None, 2, None, 3])
    tree.printTree()



