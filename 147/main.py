from typing import List

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

    def __eq__(self, other):
        if self.val != other.val:
            return False
        return self.next == other.next

# array to nodes
def array_to_nodes(a):
    if len(a) == 0:
        return None
    return ListNode(a[0], array_to_nodes(a[1:]))

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        last = head
        cur = head.next
        head = ListNode(0, head)

        while cur:
            if last.val > cur.val:
                hh = head
                while hh.next.val < cur.val:
                    hh = hh.next

                last.next = cur.next

                tmp = hh.next
                hh.next = cur
                cur.next = tmp

                cur = last.next
            else:
                last = cur
                cur = cur.next

        return head.next


def test(head, ans):
    s = Solution()
    r = s.insertionSortList(head)
    if r != ans:
        print('inp=', r)
        print('ans=', ans)

a = array_to_nodes([4, 2, 1, 3])
b = array_to_nodes([1, 2, 3, 4])
test(a,b)

test(ListNode(), ListNode())

test(None, None)

a = array_to_nodes([4, 2, 1, 3, 5])
b = array_to_nodes([1, 2, 3, 4, 5])
test(a,b)
