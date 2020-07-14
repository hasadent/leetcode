from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        n = self.next
        s = str(self.val)
        while n:
            s += ' -> ' + str(n.val)
            n = n.next
        return s

    def __eq__(self, other):
        s = self
        o = other

        while s:
            if o is None:
                return False
            if s.val != o.val:
                return False
            s = s.next
            o = o.next
        return o == None

    @staticmethod
    def fromList(array: List):
        c = h = ListNode()
        for v in array:
            c.next = ListNode(v)
            c = c.next
        return h.next

if  __name__ == '__main__':
    assert str(ListNode.fromList([1,2,3])) == '1 -> 2 -> 3'

    assert ListNode.fromList([]) == None

    h = ListNode.fromList([1])
    assert h.val == 1 and h.next == None

    h = ListNode.fromList([1,2,3])
    assert h.val == 1
    assert h == ListNode(1, ListNode(2, ListNode(3)))
    assert h.next.val == 2
    assert h.next == ListNode(2, ListNode(3))

    assert (ListNode.fromList([1,2,3]) == ListNode.fromList([1,2])) == False
    assert (ListNode.fromList([1,2,3]) == None) == False
    assert (None == ListNode.fromList([1,2,3])) == False
    assert (ListNode.fromList([1,2]) == ListNode.fromList([1,2,3])) == False

