# The Boyer–Moore majority vote algorithm is an algorithm
# for finding the majority of a sequence of elements using
# linear time and a constant number of words of memory.

def BoyerMooreVotingAlgorithm(arr): 
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    majElem, count = arr[0], 1
    for elem in arr[1:]:
        if elem == majElem:
            count += 1
        else:
            count -= 1
            if count == 0:
                majElem = elem
                count = 1
    return majElem    
        