import sys
sys.path.append('../common')
from TreeNode import TreeNode
from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        v = preorder.pop(0)
        x = inorder.index(v)
        l = self.buildTree(preorder, inorder[0:x])
        r = self.buildTree(preorder, inorder[x+1:])
        return TreeNode(v, l, r)


def test(preorder, inorder, ans):
    s = Solution()
    r = s.buildTree(preorder, inorder)
    if r != ans:
        print('mine')
        r.printTree(1)
        print('ans')
        ans.printTree(1)



test([3,9,20,15,7], [9,3,15,20,7], TreeNode.fromList([3, 9, 20, None, None, 15, 7]))


