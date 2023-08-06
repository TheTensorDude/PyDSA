# Quicksort implementation using recursion
# Know more about quicksort from https://en.wikipedia.org/wiki/Quicksort

# Time complexity: O(n.log(n)) | Space complexity: O(log(n))

# swapping operation    
def swap(index1: int, index2: int, arr: list):
    arr[index1], arr[index2] = arr[index2], arr[index1] 

def quicksort(arr: list):
    """
    Recursive implementation of QuickSort
    """
    quicksortHelper(arr, 0, len(arr) - 1)
    return arr    

def quicksortHelper(arr: list, startIndex : int, endIndex : int):
    # base case: if endIndex < startIndex then it means we are done exploring
    if endIndex <= startIndex:
        return 
    
    # Pivot will be the first item in the array
    pivotIndex = startIndex
    # left index will be the consequitive right item of pivot
    leftIndex = startIndex + 1
    # rightIndex is the last item of the array
    rightIndex = endIndex
    
    while leftIndex <= rightIndex:
        
        # we need to put items that are greater than the pivot to the right and vice-versa
        # as eventually the pivot element will be swapped by the rightIndex element
        if arr[leftIndex] > arr[pivotIndex] and arr[rightIndex] < arr[pivotIndex]:
            swap(leftIndex, rightIndex, arr)

        # if leftIndex is less than the pivot index, we are alright
        # just increment the leftIndex
        elif arr[leftIndex] < arr[pivotIndex]:
            leftIndex += 1
            
        # if rightIndex if greater than pivot, we are alright. 
        # Just decrease the right index
        elif arr[rightIndex] > arr[pivotIndex]:
            rightIndex -= 1
            
    # swaping the rightIndex with the pivot
    # rightIndex will always carry an item which is < than the pivot        
    swap(rightIndex, pivotIndex, arr)
    
    # performing quicksort on the left subarray
    quicksortHelper(arr, startIndex, rightIndex - 1)
    # performing quicksort on the right subarray
    quicksortHelper(arr, leftIndex + 1, endIndex)
    

print(quicksort([5, 6, 2, 1, 56]))
    
    