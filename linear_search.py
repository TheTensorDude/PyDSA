# Given an element and an array, return the index where the element is present in the array
# return False if element if not present

# Solution: Linear search
# Time complexity: O(N), Space complexity: O(1)
def linearSearch(arr: list, element: int):
    for index, value in enumerate(arr):
        if value == element:
            return index 
    return False