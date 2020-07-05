import sys
sys.path.append('../common')
from TreeNode import TreeNode

class Codec:

    def serialize(self, root):
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

    def deserialize(self, data):
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


def test(root):
    codec = Codec()

    print('input')
    root.printTree(4)

    r0 = codec.serialize(root)
    print('serialize', r0)
    r1 = codec.deserialize(r0)
    print('deserialize')
    r1.printTree(4)


test(TreeNode.fromList([1,2,3,None,None,4,5]))

test(TreeNode.fromList([-1,0,1]))
