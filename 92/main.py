from typing import List

# array to nodes
def array_to_nodes(a):
    if len(a) == 0:
        return None
    return ListNode(a[0], array_to_nodes(a[1:]))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        n = self.next
        s = str(self.val)
        while n:
            s += '->' + str(n.val)
            n = n.next
        return s

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        h = ListNode(0, head)

        m -= 1
        list0_end = h

        i = 0
        while i < m:
            list0_end = list0_end.next
            i += 1

        revhead = list0_end.next
        revtail = list0_end
        while i < n:
            revtail = revtail.next
            i += 1

        list1_head = revtail.next
        revtail.next = None
        while revhead:
            temp = revhead.next
            revhead.next = list1_head
            list1_head = revhead
            revhead = temp

        list0_end.next = list1_head
        return h.next



def test(head, m, n):

    s = Solution()
    r = s.reverseBetween(head, m, n)

    print(r)

test(array_to_nodes([1,2,3,4,5]), 2, 4)
