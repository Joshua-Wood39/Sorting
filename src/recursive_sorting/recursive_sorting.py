# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    c = 0
    while a < len(arrA) and b < len(arrB):
        if(arrA[a] < arrB[b]):
            merged_arr[c] = arrA[a]
            a += 1
            print(f"a: {a}, b: {b}, c: {c}, merged: {merged_arr}")
        else:
            print(merged_arr)
            merged_arr[c] = arrB[b]
            b += 1
            print(f"a: {a}, b: {b}, c: {c}, merged: {merged_arr}")
        c += 1

    while a < len(arrA):
        merged_arr[c] = arrA[a]
        a += 1
        c += 1
        print(f"a: {a}, b: {b}, c: {c}, merged: {merged_arr}")

    while b < len(arrB):
        merged_arr[c] = arrB[b]
        b += 1
        c += 1
        print(f"a: {a}, b: {b}, c: {c}, merged: {merged_arr}")

    print(f'merged: {merged_arr}')
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

    # this recursion and the function above are the only difference...
        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] <= right[b]:
                arr[c] = left[a]
                a += 1
            else:
                arr[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
