from typing import Optional, List
# TODO


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = qo = rem = 0
        llist = ListNode(0)
        if not l1 or not l2:
            return l1 or l2
        while l1 and l2:
            temp = l1.val + l2.val
            qo = temp // 10
            rem = temp % 10
            llist.val = rem + total
            llist.next = l1.next
            if qo > 0:
                total = qo
            l1, l2 = l1.next, l2.next
        if l1:
            print("remaining l1")
        else:
            print("remaining l2")
        return l1


if __name__ == '__main__':
    l1 = LinkedList()
    l1.head = ListNode(9)
    v1 = ListNode(9)
    v2 = ListNode(9)

    l2 = LinkedList()
    l2.head = ListNode(9)
    v3 = ListNode(9)
    v4 = ListNode(9)
    v5 = ListNode(9)
    v6 = ListNode(8)

    l1.head.next, v1.next = v1, v2
    l2.head.next, v3.next = v3, v4
    sol = Solution().addTwoNumbers(l1.head, l2.head)
