def item_in_common(list1, list2):
    my_dict = {}
    for num in list1:
        my_dict[num] = True
    for num in l2:
        if num in my_dict:
            return True
    return False


l1 = [1, 2, 4, 7, 9]
l2 = [3, 6, 5, 9]
print(item_in_common(l1, l2))