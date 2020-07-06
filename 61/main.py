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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        c = 1
        t = head
        n = head.next
        while n:
            c += 1
            t = n
            n = n.next

        k %= c
        if k == 0:
            return head
        k = c - k - 1

        n = head
        while k > 0:
            n = n.next
            k -= 1

        t.next = head
        head = n.next
        n.next = None
        return head

def test(head, k, ans):
    head = array_to_nodes(head)
    ans = array_to_nodes(ans)

    s = Solution()
    r = s.rotateRight(head, k)

    if r != ans:
        print('not correct: %d %s %s' % (k, r, ans))


test([1,2,3,4,5], 2, [4,5,1,2,3])
test([0,1,2], 4, [2,0,1])
test([0,1,2], 6, [0,1,2])

