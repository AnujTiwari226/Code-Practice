class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        nhead = head
        while fast and fast.next:
            nhead = nhead.next
            fast = fast.next.next
        prev = nhead
        nhead = nhead.next
        prev.next = None
        while nhead:
            next = nhead.next
            nhead.next = prev
        prev = nhead
        nhead = next

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
