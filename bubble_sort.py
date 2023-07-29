# Implements Bubble sort
# Know more about bubble sort from https://en.wikipedia.org/wiki/Bubble_sort

# swapping operation    
def swap(index1: int, index2: int, arr: list):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    
# Time complexity: O(N^2), Space complexity: O(1)
def BubbleSort(arr: list):
    counter = 0
    lastIndex = len(arr) - 1
    while counter <= lastIndex:
        for idx in range(0, lastIndex - counter):
            if arr[idx] > arr[idx + 1]:
                swap(idx, idx + 1, arr)
        counter += 1        
    return arr