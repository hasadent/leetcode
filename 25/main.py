import sys
sys.path.append('../common')

from ListNode import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        p = c = head = ListNode(0, head)
        while c:
            for _ in range(k):
                c = c.next
                if not c:
                    return head.next

            h, t = None, p.next
            while p.next != c:
                x = p.next

                p.next = x.next                                
                x.next = h
                h = x

            t.next = c.next
            c.next = h
            p.next = c

            p = c = t

def test(head_list, k, ans_list):

    head = ListNode.fromList(head_list)
    ans = ListNode.fromList(ans_list)

    s = Solution()
    r = s.reverseKGroup(head, k)
    if r != ans:
        print('not correct', head_list, k, r, ans)


test([1,2,3,4,5], 2, [2,1,4,3,5])
test([1,2,3,4,5], 3, [3,2,1,4,5])
test([1,2], 3, [1,2])
test([], 4, [])
test([1,2,3,4,5], 1, [1,2,3,4,5])
