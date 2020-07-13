import sys
sys.path.append('../common')

from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = nth = head
        for _ in range(n + 1):
            if nth == None:
                return head.next
            nth = nth.next

        while nth:
            p = p.next
            nth = nth.next

        p.next = p.next.next
        return head



def test(head_list, n, ans_list):

    head = ListNode.fromList(head_list)
    ans = ListNode.fromList(ans_list)

    s = Solution()
    r = s.removeNthFromEnd(head, n)
    if r != ans:
        print('not correct', head_list, n, r, ans)


test([1,2,3,4,5], 2, [1,2,3,5])
test([1], 1, [])
test([1,2], 2, [2])
test([1,2], 1, [1])
