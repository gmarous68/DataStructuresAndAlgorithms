def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        k = i - 1
        while temp < arr[k] and k >= 0:
            arr[k + 1] = arr[k]
            arr[k] = temp
            k -= 1
    return arr


arr = [2, 1, 4, 5, 3, 1, 6, 2]
print(insertion_sort(arr))
