def binary_search(arr, srch_v, lo, hi):

    mid = lo + int((hi - lo)/2)

    arr_v = arr[mid]

    if srch_v == arr_v:
        return mid
    if srch_v > arr_v:
        mid = binary_search(arr, srch_v, mid, hi)
    if srch_v < arr_v:
        mid = binary_search(arr, srch_v, lo, mid)
    
    return mid


arr = [1, 4, 23, 45, 56, 67, 78, 89, 100, 123, 345, 567]
print(binary_search(arr, 1, 0, len(arr)))
print(binary_search(arr, 4, 0, len(arr)))
print(binary_search(arr, 23, 0, len(arr)))
print(binary_search(arr, 45, 0, len(arr)))
print(binary_search(arr, 56, 0, len(arr)))
print(binary_search(arr, 67, 0, len(arr)))
print(binary_search(arr, 78, 0, len(arr)))
print(binary_search(arr, 89, 0, len(arr)))
print(binary_search(arr, 100, 0, len(arr)))
print(binary_search(arr, 123, 0, len(arr)))
print(binary_search(arr, 345, 0, len(arr)))
print(binary_search(arr, 567, 0, len(arr)))
