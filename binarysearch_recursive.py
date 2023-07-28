# Recursive implementation of Binary search
# Do not know Binary search? Refer https://en.wikipedia.org/wiki/Binary_search_algorithm

def recursiveBinarySearch(arr: list, target: int, left: int, right: int):
    # as the array is sorted, so left pointer >  right pointer means
    # the target element is not there
    if left > right:
        return "Target is not present"
    
    # calculating the middleIndex
    midIndex = (left + right) // 2
    # if we are going to find the target, then it will always going 
    # to be in the midIndex
    potentialMatch = arr[midIndex]
    if target == potentialMatch:
        return midIndex
    
    # remember the array is sorted
    # so if the target is less than the potential match then it must be on the
    # left hand side of the midIndex, we do not want to explore midIndex as we
    # have done it already
    elif target < potentialMatch:
        return recursiveBinarySearch(arr, target, 0, midIndex - 1)
    
    # opposive of the above, if the target is greater than the mid value then
    # the items thart are on the right are worth exploring
    else:
        return recursiveBinarySearch(arr, target, midIndex + 1, right)