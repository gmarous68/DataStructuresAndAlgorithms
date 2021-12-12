def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_idx]:
                min_idx = k
        if i != min_idx:
            temp = arr[min_idx]
            arr[min_idx] = arr[i]
            arr[i] = temp
    return arr


my_list = [3, 6, 8, 9, 2, 5, 10, 2, 7]
print(selection_sort(my_list))
