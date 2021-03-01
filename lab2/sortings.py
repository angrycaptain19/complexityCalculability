# library for all the sortings and utilities

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
# end of swap function


def bubbleSort(array):
    if len(array) == 1:
        return

    swapped = True
    for i in range(len(array) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                swapped = True
            yield array
# end of bubbleSort function


def getNextGap(gap):
    gap /= 1.3
    if gap < 1:
        return 1
    return gap


def combSort(array):

    n = len(array)
    gap = n
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped == 1:

        # Find next gap
        gap = getNextGap(gap)

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        gap = int(gap)
        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
            yield array
# end of combSort function

def insertionSort(array):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
            yield array
# end of insertionSort function

def selectionSort(array):
    
    if len(array) == 1:
        return

    for i in range(len(array)):
        minVal = array[i]
        minIdx = i
        for j in range(i, len(array)):
            if array[j] < minVal:
                minVal = array[j]
                minIdx = j
            yield array
        swap(array, i, minIdx)
        yield array
# end of selectionsort function

def mergeSort(array, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeSort(array, start, mid)
    yield from mergeSort(array, mid + 1, end)
    yield from merge(array, start, mid, end)
    yield array
# end of mergeSort function


def merge(array, start, mid, end):
    merged = []
    leftIndex = start
    rightIndex = mid + 1

    while leftIndex <= mid and rightIndex <= end:
        if array[leftIndex] < array[rightIndex]:
            merged.append(array[leftIndex])
            leftIndex += 1
        else:
            merged.append(array[rightIndex])
            rightIndex += 1

    while leftIndex <= mid:
        merged.append(array[leftIndex])
        leftIndex += 1

    while rightIndex <= end:
        merged.append(array[rightIndex])
        rightIndex += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array
# end of merge function


def quickSort(array, start, end):
    if start >= end:
        return

    pivot = array[end]
    pivotIndex = start

    for i in range(start, end):
        if array[i] < pivot:
            swap(array, i, pivotIndex)
            pivotIndex += 1
        yield array
    swap(array, end, pivotIndex)
    yield array

    yield from quickSort(array, start, pivotIndex - 1)
    yield from quickSort(array, pivotIndex + 1, end)
# end of quickSort function


def heapify(array, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    while left < n and array[left] > array[largest]:
        largest = left
    while right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        swap(array, i, largest)
        yield array
        yield from heapify(array, n, largest)
# end of heapify function


def heapSort(array):
    size = len(array)
    for i in range(size, -1, -1):
        yield from heapify(array, size, i)
    for i in range(size - 1, 0, -1):
        swap(array, 0, i)
        yield array
        yield from heapify(array, i, 0)
# end of heapSort function
