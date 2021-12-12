from linkedlist.DoublyNode import DoublyNode


class DoublyLinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.num_nodes = 0

    def is_empty(self):
        return self.first is None

    def get(self, idx):
        if self.is_empty():
            print("Linked list is empty..")
            return None
        if idx == 0:
            return self.first
        if idx == self.num_nodes - 1:
            return self.last
        if 0 < idx < self.num_nodes:
            if idx < self.num_nodes / 2:
                temp = self.first
                for _ in range(idx):
                    temp = temp.next
                return temp
            else:
                temp = self.last
                for _ in range(self.num_nodes - 1, idx, -1):
                    temp = temp.previous
                return temp
        return None

    def set_value(self, idx, value):
        temp = self.get(idx)
        if temp:
            temp.value = value
            return "Value changed to " + str(value) + " in idx: " + str(idx)
        return "No node with index: " + str(idx)

    def insert(self, idx, value):
        if self.is_empty() or idx == 0:
            self.prepend(value)
            return
        if 0 > idx >= self.num_nodes:
            return
        if idx == self.num_nodes:
            self.append(value)
            return
        temp = self.get(idx)
        new_node = DoublyNode(value)
        new_node.next = temp
        new_node.previous = temp.previous
        temp.previous.next = new_node
        temp.previous = new_node
        self.num_nodes += 1

    def remove(self, idx):
        if idx == 0:
            self.pop_first()
            return
        if idx == self.num_nodes - 1:
            self.pop_last()
            return
        prev = self.get(idx - 1)
        temp = prev.next
        prev.next = temp.next
        temp.previous = None
        temp = temp.next
        temp.previous = prev
        self.num_nodes -= 1

    def prepend(self, value):
        new_node = DoublyNode(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.previous = new_node
            self.first = new_node
        self.num_nodes += 1

    def append(self, value):
        new_node = DoublyNode(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.previous = self.last
            self.last.next = new_node
            self.last = new_node
            new_node.next = None
        self.num_nodes += 1

    def pop_last(self):
        if self.is_empty():
            print("Linked list is empty..")
            return
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.last.previous
            temp.next.previous = None
            self.last = temp
            self.last.next = None
        self.num_nodes -= 1

    def pop_first(self):
        if self.is_empty():
            print("Linked list is empty..")
            return
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = temp.next
            self.first.previous = None
            temp.next = None
        self.num_nodes -= 1

    def print_num_nodes(self):
        return self.num_nodes

    def print_me(self):
        if self.is_empty():
            print("\nLinked list is empty..")
            return
        temp = self.first
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()
