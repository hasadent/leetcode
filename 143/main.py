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

    def __eq__(self, other):

        if self.val != other.val:
            return False
        return self.next == other.next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        h = head
        stack = []
        count = 0
        while h:
            stack.append(h)
            h = h.next
            count += 1

        count = (count - 1) // 2

        h = head
        while count > 0:
            n = stack.pop()

            n.next = h.next
            h.next = n
            h = h.next.next
            count -= 1

        n = stack.pop()
        n.next = None

def test(head, answer):
    s = Solution()

    s.reorderList(head)

    if head != answer:
        print('mine:   %s' % head)
        print('answer: %s' % answer)

test(array_to_nodes([1,2,3,4]), array_to_nodes([1,4,2,3]))
test(array_to_nodes([1,2,3,4,5]), array_to_nodes([1,5,2,4,3]))
test(array_to_nodes([1,2,3,4,5,6]), array_to_nodes([1,6,2,5,3,4]))
