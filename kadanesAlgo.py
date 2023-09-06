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