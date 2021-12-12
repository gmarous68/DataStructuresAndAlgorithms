from Node import Node


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return
        if self.top.next is None:
            self.top = None
            return
        temp = self.top
        self.top = self.top.next
        temp.next = None

    def print_stack(self):
        if self.top is None:
            return
        temp = self.top
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()