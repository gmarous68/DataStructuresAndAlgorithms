from linkedlist.DoublyLinkedList import DoublyLinkedList

my_list = DoublyLinkedList()

my_list.prepend(10)
my_list.prepend(20)
my_list.prepend(30)
my_list.prepend(40)
my_list.prepend(50)
my_list.prepend(60)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

my_list.append(10)
my_list.append(20)
my_list.append(30)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

my_list.pop_last()
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

my_list.pop_first()
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

idx = 4
temp = my_list.get(idx)
txt = "Value at idx: " + str(idx) + " is: " + str(temp.value) if temp else "No node with idx: " + str(idx)
print(txt)
print('*' * 45)

print(my_list.set_value(0, 1000))
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

my_list.insert(0, 2000)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
my_list.insert(8, 5000)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)

my_list.remove(0)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
my_list.remove(7)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
my_list.remove(1)
print("no of nodes:", str(my_list.print_num_nodes()), end=": ")
my_list.print_me()
print('*' * 45)
