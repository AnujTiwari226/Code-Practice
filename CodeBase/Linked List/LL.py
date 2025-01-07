class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self, data):
        self.head = Node(data)

    def insert_first(self, data):
        if not self.head:
            self.head.data = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def insert_at_middle(self, target, data):
        if not self.head:
            print('target not exist')
            return None
        temp = self.head
        t = None
        while temp and temp.data != target:
            temp = temp.next
        if not temp:
            print('Target is not in the list')
            return
        node = Node(data)
        node.next = temp.next
        temp.next = node

    def insert_in_the_end(self, data):
        if not self.head:
            self.head = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(data)
        temp.next = node
        node.next = None

    def delete_first(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def display(self):
        node = self.head
        while node:
            print(node.data, '-> ', end='')
            node = node.next
        print('End')

    def delete_from_last(self):
        if not self.head:
            return None
        elif not self.head.next:
            val = self.head.data
            self.head = None
            return val
        node = self.head
        while node.next.next:
            node = node.next
        val = node.next.data
        node.next = None
        return val

    def delete_from_middle(self, target):
        if not self.head:
            return self.head
        prev = self.head
        node = self.head
        while node and node.data != target:
            prev = node
            node = node.next
        if not node:
            print('Target not int the list')
            return
        prev.next = node.next
        return node.data






