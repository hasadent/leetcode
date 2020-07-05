import sys
sys.path.append('../common')
from TreeNode import TreeNode
from typing import List

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None

        node = TreeNode(pre[0])
        if len(pre) != 1:
            x = post.index(pre[1]) + 1
            node.left = self.constructFromPrePost(pre[1:x+1], post[0:x])
            node.right =self.constructFromPrePost(pre[x+1:], post[x:-1])

        return node


def test(pre, post, ans):
    s = Solution()
    r = s.constructFromPrePost(pre, post)
    if r != ans:
        print('mine')
        r.printTree(1)
        print('ans')
        ans.printTree(1)
        print(ans)


test([1,2,4,5,3,6,7], [4,5,2,6,7,3,1], TreeNode.fromList([1,2,3,4,5,6,7]))


