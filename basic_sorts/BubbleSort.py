def bubble_sort(arr):
    sort = True
    while sort:
        sort = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                sort = True
    return arr


my_list = [3, 6, 8, 9, 2, 5, 10, 2, 7]

print(bubble_sort(my_list))
