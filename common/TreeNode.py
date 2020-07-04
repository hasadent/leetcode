from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = ' [ ' + str(self.val)

        if self.left:
            s += str(self.left)

        if self.right:
            s += str(self.right)
        s += ' ] '
        return s

    @staticmethod
    def fromList(array):
        if len(array) == 0:
            return None

        v = array.pop(0) 
        r = TreeNode(v)
        queue = [r]
        while len(array) > 0:
            n = queue.pop(0)

            v = array.pop(0)
            if v:
                n.left = TreeNode(v)
                queue.append(n.left)

            if array:
                v = array.pop(0)
                if v:
                    n.right = TreeNode(v)
                    queue.append(n.right)

        return r

    def printTree(self):
        ident = [ 0 ]
        queue = [ (0, self) ]
        
        while queue:
            ident, n = queue.pop(0)

            s = ' ' * ident
            if n == self:
                s += 'o %3d' % n.val
                ident += 5
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
                    queue.append((ident, n.right))
                nn = nn.left

            print(s)


if __name__ == '__main__':
    tree = TreeNode.fromList([3,9,20,None,None,15,7])
    tree.printTree()

    tree = TreeNode.fromList([1, None, 2, None, 3])
    tree.printTree()



