import sys
sys.path.append('../common')
from TreeNode import TreeNode
from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        v = postorder.pop()
        x = inorder.index(v)
        r = self.buildTree(inorder[x+1:], postorder)
        l = self.buildTree(inorder[0:x], postorder) 
        return TreeNode(v, l, r)


def test(preorder, inorder, ans):
    s = Solution()
    r = s.buildTree(preorder, inorder)
    if r != ans:
        print('mine')
        r.printTree(1)
        print('ans')
        ans.printTree(1)


test([9,3,15,20,7], [9,15,7,20,3], TreeNode.fromList([3, 9, 20, None, None, 15, 7]))


