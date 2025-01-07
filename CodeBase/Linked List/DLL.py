class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            node.prev = None

    def insert_in_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.next = None
            node.prev = temp

    def display(self):
        if not self.head:
            print('Empty List')
        node = self.head
        while node:
            print(node.data, '-> ', end='')
            node = node.next

        print('End')

    def insert_in_middle(self, target, data):
        if not self.head:
            print('Empty List, can\'t add after target as its missing')
            return
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if not temp:
            print('Target missing from List')
            return
        node = Node(data)
        node.next = temp.next
        if temp.next:
            temp.next.prev = node
        temp.next = node
        node.prev = temp

    def delete_first(self):
        if not self.head:
            print("List is empty already")
            return

        val = self.head.data
        if not self.head.next:
            self.head = None
            return val
        else:
            self.head = self.head.next
            self.head.prev = None
            return val

    def delete_from_middle(self,target, data):
        pass

    def delete_from_end(self):
        pass


