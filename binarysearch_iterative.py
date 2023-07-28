# Recursive implementation of Binary search
# Do not know Binary search? Refer https://en.wikipedia.org/wiki/Binary_search_algorithm

# Time complexity: O(log(N)), Space complexity: O(1)
def BinarySearch(arr: list, target: int):
    # left and right pointers
    left = 0
    right = len(arr) - 1

    while left <= right:
        # The only way we are going to find our target is from this midIndex
        midIndex = (left + right) // 2
        potentialMatch = arr[midIndex]
        if target == potentialMatch:
            return midIndex
        
        # remember the array is sorted
        # so if the target is less than the potential match then it must be on the
        # left hand side of the midIndex, we do not want to explore midIndex as we
        elif target < potentialMatch:
            right = midIndex - 1
            
        # opposive of the above, if the target is greater than the mid value then
        # the items thart are on the right are worth exploring
        else:
            left = midIndex + 1            
        