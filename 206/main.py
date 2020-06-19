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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h = None

        while head:
            t = head.next
            head.next = h
            h = head
            head = t

        return h

def test(head):
    s = Solution()
    r = s.reverseList(head)

    print(r)

test(None)
test(array_to_nodes([1,2,3,4,5]))

