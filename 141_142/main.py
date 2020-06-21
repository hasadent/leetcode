from typing import List

# array to nodes
def array_to_nodes(a):
    if len(a) == 0:
        return None
    return ListNode(a[0], array_to_nodes(a[1:]))

def nodes_add_cycle(head, index):
    if index < 0:
        return head

    h = head
    i = 0
    c = None

    while h:
        if i == index:
            c = h
        if not h.next:
            h.next = c
            break
        h = h.next
        i += 1

    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow = fast = head

        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # note 1
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
'''
*** 1 ***

    C: cycle length
    L: distance bewteen list head and cycle head
    d: distance of slow to cycle head

    fast => 2 x step = n x C + L + d ... (1)
    slow => 1 x step = L + d         ... (2)

    2 x (L + d) =  = n x C + L + d   ... from (1) and (2)
    L = n x C - d

    slow left to head => C - d
'''

def test(head, a0, a1):
    s = Solution()

    r0 = s.hasCycle(head)
    r1 = s.detectCycle(head)


    r1v = r1.val if r1 else -1

    if r0 == a0 and r1v == a1:
        return
    print('not correct')
    print('hasCycle => %s %s' % (r0, a0))
    print('detectCycle => %s %s' % (r1v, a1))


inp = nodes_add_cycle(array_to_nodes([3,2,0,-4]),1)
test(inp, True, 2)

inp = nodes_add_cycle(array_to_nodes([1, 2]),0)
test(inp, True, 1)

inp = nodes_add_cycle(array_to_nodes([1]),-1)
test(inp, False, -1)


