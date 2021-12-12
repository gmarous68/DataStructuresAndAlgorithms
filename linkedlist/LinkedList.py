from linkedlist.Node import Node


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.num_of_nodes = 0

    def is_empty(self):
        return self.first is None

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.num_of_nodes += 1
        return True

    def pop_first(self):
        if self.is_empty():
            return False
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
        self.num_of_nodes -= 1
        return True

    def pop_last(self):
        if self.is_empty():
            return
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            while temp.next is not self.last:
                temp = temp.next
            self.last = temp
            self.last.next = None
        self.num_of_nodes -= 1

    def set_value(self, idx, value):
        if self.is_empty():
            return True
        node = self.get(idx)
        if node:
            node.value = value
            return True
        return False

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.last = new_node
            self.first = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.num_of_nodes += 1
        return True

    def get(self, idx):
        if self.is_empty():
            return None
        if idx == 0:
            return self.first
        if idx == self.num_of_nodes - 1:
            return self.last
        if 0 < idx <= self.num_of_nodes - 1:
            temp = self.first
            for _ in range(idx):
                temp = temp.next
            return temp
        return None

    def remove(self, idx):
        if idx == 0:
            return self.pop_first()
        if idx == self.num_of_nodes - 1:
            return self.pop_last()
        if not self.get(idx):
            return False

        prev = self.get(idx - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.num_of_nodes -= 1
        return True

    def reverse(self):
        if self.is_empty() or self.first == self.last:
            return None

        temp = self.first
        self.first = self.last
        self.last = temp
        before = None
        for _ in range(self.num_of_nodes):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def insert(self, idx, value):
        if idx < 0 or idx > self.num_of_nodes:
            return False
        if idx == 0:
            return self.prepend(value)
        if idx == self.num_of_nodes:
            return self.append(value)

        temp = self.get(idx - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.num_of_nodes += 1
        return True

    def print_list(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
