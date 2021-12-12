from Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.no_of_nodes = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return
        if self.first is self.last:
            self.first = None
            self.last = None
            return
        temp = self.first
        self.first = self.first.next
        temp.next = None

    def print_me(self):
        if self.first is None:
            return
        temp = self.first
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()
