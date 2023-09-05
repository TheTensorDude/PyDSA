# Kadane's Algorithm is a dynamic programming technique used to find the maximum subarray
# sum in an array. It's an efficient way to solve this problem with a time complexity of O(n),
# where n is the length of the array. Here's a Python implementation of Kadane's Algorithm:

def kadanesAlgo(arr):
    currSum = 0
    maxSum = float("-inf")
    for num in arr:
        currSum = max(0, currSum + num)
        maxSum = max(currSum, maxSum)
    return maxSum


# Test case 1: Array with all positive elements
arr1 = [1, 2, 3, 4, 5]
result1 = kadanesAlgo(arr1)
# Expected output: 15 (the entire array is the maximum subarray)

# Test case 2: Array with all negative elements
arr2 = [-5, -4, -3, -2, -1]
result2 = kadanesAlgo(arr2)
# Expected output: -1 (choosing the maximum negative value)

# Test case 3: Array with a single element
arr3 = [7]
result3 = kadanesAlgo(arr3)
# Expected output: 7 (the only element is the maximum subarray)

# Test case 4: Array with alternating positive and negative elements
arr4 = [1, -2, 3, -4, 5, -6]
result4 = kadanesAlgo(arr4)
# Expected output: 5 (corresponding to the subarray [5])

# Test case 5: Array with all zeros
arr5 = [0, 0, 0, 0, 0]
result5 = kadanesAlgo(arr5)
# Expected output: 0 (choosing an empty subarray)

# Test case 6: Array with mixed positive and negative elements
arr6 = [2, -3, 4, -1, -2, 1, 5, -3]
result6 = kadanesAlgo(arr6)
# Expected output: 8 (corresponding to the subarray [4, -1, -2, 1, 5])

# Test case 7: Large array with random values
arr7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 7, -4, 3, 2, -1]
result7 = kadanesAlgo(arr7)
# Expected output: 13 (corresponding to the subarray [4, -1, 2, 1, -5, 4, 7])
