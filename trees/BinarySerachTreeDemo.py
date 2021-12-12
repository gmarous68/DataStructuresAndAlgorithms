from BinarySearchTree import BinarySearchTree

#create tree object
my_bst = BinarySearchTree()

my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(27)
my_bst.insert(52)
my_bst.insert(82)

if my_bst.root is not None:
    print(my_bst.root.value, end=" ")
    if my_bst.root.left is not None:
        print(my_bst.root.left.value, end=" ")
    if my_bst.root.right is not None:
        print(my_bst.root.right.value)

print(my_bst.contains(27))
print(my_bst.contains(18))
print(my_bst.contains(21))
print(my_bst.contains(83))

print("Minimum value left branch in BST is:", my_bst.search_minimum(my_bst.root))
if my_bst.root is not None and my_bst.root.right is not None:
    print("Minimum value left branch in BST is:", my_bst.search_minimum(my_bst.root.right))

print(my_bst.bfs())
print(my_bst.dfs_pre_order())
print(my_bst.dfs_post_order())
print(my_bst.dfs_in_order())
