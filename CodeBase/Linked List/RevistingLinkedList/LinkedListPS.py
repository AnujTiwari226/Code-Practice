from BasicSinglyLinkedListSolutions import BasicSolution

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(BasicSolution):
    def __init__(self, val):
        super().__init__(val)
    def get_curr_head(self):
        return self.head
    def RemoveDuplicate(self, head):
        if not head:
            return head
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

    def delete_node(self, target, head):
        if not self.head:
            return None
        node = self.head
        while node and node.val != target:
                node = node.next
        if not node:
            return
        temp = node
        node.next = temp.next
        return temp.val