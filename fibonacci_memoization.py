# Given an integer N, return the Nth number in the fibonacci series.
# Fibonacci series: 0,1,1,2,3,5,8,13,21,34,55,89,144......

# This solution uses memoization
# Time complexity: O(N), Space complexity: O(N)
def getNthFibonacci(n: int, memoization: dict = {1 : 0, 2: 1}) -> int:
    if n in memoization.keys():
        return memoization[n]
    else:
        memoization[n] = getNthFibonacci(n - 1, memoization) + getNthFibonacci(n - 2, memoization)
        return memoization[n]