# Selection sort implementation in Python
# Know more from https://en.wikipedia.org/wiki/Selection_sort

# swapping operation    
def swap(index1: int, index2: int, arr: list):
    arr[index1], arr[index2] = arr[index2], arr[index1] 
    
    
# Time complexity: O(N^2), Space complexity: O(1)
def selection_sort(arr: list):
    currIndex = 0
    # iterating through the entire arr 
    while currIndex < len(arr) - 1:
        # assume the current index is the smallest in the array
        smallestIdx = currIndex
        # iterating through the index currIndex + 1 to last index
        # if any of these elements are > than our assumed smallestValue
        # we need to update the index
        for i in range(currIndex + 1, len(arr)):
            if arr[i] < arr[smallestIdx]:
                smallestIdx = i 
        # swap eventually, with or without update
        swap(currIndex, smallestIdx, arr)
        # increment the pointer
        currIndex += 1
    return arr