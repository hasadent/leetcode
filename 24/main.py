import sys
sys.path.append('../common')

from ListNode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        c = h = ListNode(0, head)
        head = head.next
        while c:
            c = c.next
            if not c:
                break
            c = c.next
            if not c:
                break

            h.next.next = c.next
            c.next = h.next
            h.next = c

            h = c = c.next

        return head


def test(head_list, ans_list):

    head = ListNode.fromList(head_list)
    ans = ListNode.fromList(ans_list)

    s = Solution()
    r = s.swapPairs(head)
    if r != ans:
        print('not correct', head_list, r, ans)


test([1,2,3,4], [2,1,4,3])
test([1,2,3,4,5], [2,1,4,3,5])
test([1], [1])
test([], [])
