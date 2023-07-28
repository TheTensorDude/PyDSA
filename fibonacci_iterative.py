# Given an integer N, return the Nth number in the fibonacci series.
# Fibonacci series: 0,1,1,2,3,5,8,13,21,34,55,89,144......

# This solution an iterative solution
# Time complexity: O(N), Space complexity: O(1)
def getNthFibonacci(n: int) -> int:
    lastTwo = [0, 1]
    count = len(lastTwo) + 1
    while count <= n:
        summation = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = summation
        count += 1
    return lastTwo[1] if n > 1 else lastTwo[0] 