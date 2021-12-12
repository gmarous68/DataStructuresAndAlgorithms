def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp
    return arr


def pivot(arr, pivot_idx, end_idx):
    swap_idx = pivot_idx
    for i in range(pivot_idx + 1, end_idx + 1):
        if arr[i] < arr[pivot_idx]:
            swap_idx += 1
            swap(arr, swap_idx, i)
    swap(arr, pivot_idx, swap_idx)
    return swap_idx


def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_idx = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_idx - 1)
        quick_sort_helper(arr, pivot_idx + 1, right)
    return arr


def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
