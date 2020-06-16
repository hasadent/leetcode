class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.next) + str(self.val)
        else:
            return str(self.val)
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = l1

        l1p = l1
        c = 0
        while l1 and l2:
            l1.val += l2.val + c

            c = 0            
            if l1.val >= 10:
                l1.val -= 10
                c = 1

            l1p = l1
            l1 = l1.next
            l2 = l2.next

        if not l1:
            l1p.next = l2
            l1 = l2

        while l1:
            l1.val += c

            c = 0
            if l1.val >= 10:
                l1.val -= 10
                c = 1

            l1p = l1
            l1 = l1.next

        if c != 0:
            l1p.next = ListNode(1)
        return ret

# value to node list
def v2l(v: int):
    return ListNode(int(v%10), v2l(int(v/10))) if v != 0 else None

# array to node list
def a2l(a):
    if len(a) == 0:
        return None
    return ListNode(a[-1], a2l(a[0:-1]))

def test(l1, l2):
    s = Solution()

    print()
    print('input1 = %32s' % l1)
    print('input2 = %32s' % l2)
    o = s.addTwoNumbers(l1, l2)

    print('output = %32s' % o)

test(v2l(342), v2l(465))
test(v2l(500), v2l(500))
test(v2l(1), v2l(999))
test(v2l(81), ListNode())
test(ListNode(), ListNode())
test(a2l([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]), a2l([5,6,4]))
