# Given an integer N, return the Nth number in the fibonacci series.
# Fibonacci series: 0,1,1,2,3,5,8,13,21,34,55,89,144......

# This solution is the naive solution
# Time complexity: O(2^N), Space complexity: O(N)
def getNthFibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFibonacci(n-1) + getNthFibonacci(n-2)