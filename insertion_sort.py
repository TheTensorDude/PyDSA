# Implements insertion sort
# Know more about insertion sort from https://en.wikipedia.org/wiki/Insertion_sort

# swapping operation    
def swap(index1: int, index2: int, arr: list):
    arr[index1], arr[index2] = arr[index2], arr[index1] 

# Time complexity: O(N^2) | Space complexity: O(1)
def insertionSort(arr: list):
    arrSize = len(arr)
    for i in range(1, arrSize):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(j, j - 1, arr)
            j -= 1
    return arr