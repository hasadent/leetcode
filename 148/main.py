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
        if not other:
            return False

        if self.val != other.val:
            return False
        return self.next == other.next

# array to nodes
def array_to_nodes(a):
    if len(a) == 0:
        return None
    return ListNode(a[0], array_to_nodes(a[1:]))

def mergeSort(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    head_1 = slow.next
    slow.next = None

    # sort each list
    list_0 = mergeSort(head)
    list_1 = mergeSort(head_1)

    # merge
    last = head = ListNode()

    while list_0 and list_1:
        if list_0.val > list_1.val:
            last.next = list_1
            list_1 = list_1.next
        else:
            last.next = list_0
            list_0 = list_0.next
        last = last.next

    last.next = list_0 or list_1
    return head.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return mergeSort(head)


def test(head, ans):
    s = Solution()
    r = s.sortList(head)
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
