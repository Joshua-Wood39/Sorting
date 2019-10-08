# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for index in range(len(arr) - 1):
        current = index

        for j in range(index + 1, len(arr)):
            if arr[current] > arr[j]:
                current = j

        temp = arr[index]
        arr[index] = arr[current]
        arr[current] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    counter = 0
    for i in range(0, len(arr) - 1):
        if(arr[i] > arr[i + 1]):
            temp = arr[i + 1]
            arr[i + 1] = arr[i]
            arr[i] = temp
            counter += 1

    if(counter > 0):
        bubble_sort(arr)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    highest = len(arr)
    print(f'highest: {highest}')
    for i in range(0, highest):
        print(f'\n***')
        print(f'arr[i]: {arr[i]}, i: {i}')
        temp = arr[i]
        counter = 0
        j = i + 1
        if(j > highest):
            j = highest
        k = j
        print(arr)
        while j <= len(arr) - 1:
            print(f'j: {j}')
            if(arr[j] < temp):
                temp = arr[j]
                counter += 1
                k = j
                print(f'temp: {temp}, counter: {counter}, k: {k}')
            j += 1
        if(counter != 0):
            arr[k] = arr[i]
            arr[i] = temp
            if(temp < 0):
                error = "Error, negative numbers not allowed in Count Sort"
                return error
        print(arr)
        print(f'*******\n')
    print(arr)
    return arr


# Finished MVP and Stretch
