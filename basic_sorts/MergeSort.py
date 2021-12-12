def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(l1, l2):
    combined = []
    i, k = 0, 0

    while i < len(l1) and k < len(l2):
        if l1[i] < l2[k]:
            combined.append(l1[i])
            i += 1
        else:
            combined.append(l2[k])
            k += 1
    while i < len(l1):
        combined.append(l1[i])
        i += 1
    while k < len(l2):
        combined.append(l2[k])
        k += 1
    return combined


print(merge_sort([7, 1, 9, 3, 2, 8, 5, 6]))
