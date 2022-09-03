from typing import Optional


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeElements(head.next, val=val)
        if head.data == val:
            return head.next
        else:
            return head
        # return head.next if head.data == val else head


sol1 = Solution()
sol1.head = ListNode(1)
v2 = ListNode(3)
v3 = ListNode(4)
v4 = ListNode(3)
#v5 = ListNode(5)
#v6 = ListNode(4)
sol1.head.next, v2.next, v3.next = v2, v3, v4
sol2 = sol1.removeElements(sol1.head, 3)
sol2 = sol2
