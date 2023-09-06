# Binary search for searching range in a sorted array
# Time complexity: O(logn), space complexity: O(1)
def searchRangeUsingBinarySearch(nums, target):
    lenNums = len(nums)
    low, high = 0, lenNums - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            left, right = mid, mid
            
            while (left - 1) >= 0 and nums[left - 1] == target:
                left -= 1
            
            while (right + 1) <= lenNums - 1 and nums[right + 1] == target:
                right += 1
                
            return [left, right]
            
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return [-1, -1]
        