from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class BasicSolution:
    def __init__(self, val):
        self.head = ListNode(val)
    def insert_at_beginning(self, data):
        print(f"Insert {data} before head.")
        if not self.head:
            self.head.val = ListNode(data)
        else:
            node = ListNode(data)
            node.next = self.head
            self.head = node

    def display(self):
        node = self.head
        while node:
            print(node.val, ' -> ',  end='')
            node = node.next
        print('None')

    def insert_at_middle(self, data, target):
        print(f"Insert new node [{data}] after node [{target}] in Linked List.")
        node = self.head
        while node:
            if node.val == target:
                temp = ListNode(data)
                temp.next = node.next
                node.next = temp
            node = node.next

    def insert_at_last(self, data):
        print(f"Insert {data} at the end of Linked List")
        node = self.head
        while node.next:
            if node.next:
                node = node.next

        node.next = ListNode(data)

    def delete_first(self):
        print(f"Delete First Node from Linked List")
        if not self.head:
            return None
        data = self.head.val
        self.head = self.head.next
        print(f"Deleted the First node {data} from Linked list")

    def delete_from_middle(self, target):
        print(f"!! Delete [ {target} ] node from the Linked list. !!")
        if not self.head:
            return None
        node = self.head
        while node and node.val != target:
                node = node.next
        if not node:
            print(f"Target node [ {target} ] not present in the List")
            return
        temp = node
        node.next = temp.next
        print(f"Deleted node [ {temp.val} ] from the Linked list.")
    def delete_from_last(self):
        if not self.head:
            return None
        elif not self.head.next:
            data = self.head.val
            self.head = None
            print(f"Deleted [ {data} ] from Linked list")
            return
        node = self.head
        while node.next.next:
            node = node.next
        data = node.next.val
        node.next = None
        print(f"Deleted last node i.e. [ {data} ] from the Linked list.")

    @staticmethod
    def display_list(head):
        while head:
            print(head.val, end=" -> " if head.next else "\n")
            head = head.next

    @staticmethod
    def create_multiple_linked_list(*args):
        heads = []
        for lst in args:
            if not lst:
                heads.append(None)
                continue
            head = BasicSolution.create_linked_list(lst)
            heads.append(head)
        return heads

    @staticmethod
    def create_linked_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        curr = head
        for value in lst[1:]:
            curr.next = ListNode(value)
            curr = curr.next
        return head

