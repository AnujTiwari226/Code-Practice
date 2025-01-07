from typing import Optional

from BasicSinglyLinkedListSolutions import BasicSolution, ListNode


class Solution(BasicSolution):
    def __init__(self, val):
        super().__init__(val)

    def create_ll_with_intersection(self, list1, list2, intersection):
        intersect = self.create_linked_list(intersection)
        headA = self.create_linked_list(list1)
        headA.next.next = intersect
        headB = self.create_linked_list(list2)
        headB.next.next.next = intersect
        return headA, headB

    def create_a_cycle(self, target_val):
        if not self.head:
            return None
        curr = self.head
        target = None
        last = self.head
        while curr:
            if curr.val == target_val:
                target = curr
            if not curr.next:
                last = curr
            curr = curr.next
        if last and target:
            last.next = target
        else:
            print(f"target node [ {target_val} ] not found in LinkedList")

    def display_cycle(self):
        print("Display Cyclic LinkedList")
        if not self.head:
            return None
        curr = self.head
        visited = set()
        while curr:
            if curr not in visited:
                visited.add(curr)
                print(curr.val, '->' , end='')
            else:
                print(curr.val, f'\nFound a cycle at [ {curr.val} ] node')
                return

            curr = curr.next
        print('\n')
    def hasCycle(self) -> bool:
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        this approach throws time limit exceeds error. because you're traversing both the ll once and then again travers
        the lists for finding the common node. what if both lists are of huge i.e. consist alot of nodes.
        and intersection happens at the end.
        e.g.
            headA = intersect node is at 10000 (total size is 9999, basically that means no intersection)
            headB = intersect node is at 9999 (total size is 9998, basically that means no intersection)
            you'll traverse these list for no use

        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

    @staticmethod
    def getIntersectionNodeInOptimizedWay(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        let's calculate the length of both the list first and bring both the head or prefix list i.e. before
        intersection node to same position and then compare one by one node. basically number of nodes before
        intersection should be same for comparing both nodes one by one
        :param headA:
        :param headB:
        :return:
        """
        def get_length(head):
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            return length

        if not headA or not headB:
            return None
        lenA = get_length(headA)
        lenB = get_length(headB)
        pA, pB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                pA = pA.next
        else:
            for _ in range(lenB - lenA):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA




