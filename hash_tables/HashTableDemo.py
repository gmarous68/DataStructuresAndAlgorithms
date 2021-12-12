from HashTable import HashTable

hash_table = HashTable()

hash_table.set_item('bolts', 1400)
hash_table.set_item('washers', 50)
hash_table.set_item('lumber', 70)

hash_table.print_table()
print("*" * 20)

hash_table.get_item('bolts')
hash_table.get_item('washers')
hash_table.get_item('lumber')
hash_table.get_item('lumberrrr')
print("*" * 20)

list_of_keys = hash_table.get_keys()
for key in list_of_keys:
    print(key, end=" ")
