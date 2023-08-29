# Queue is a data structure that follows FIFO (First in First out)
# This below implementation implements a queue using Linked List
# Time complexity: O(1) for both enque and deque
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next
        
class Queue:
    def __init__(self):
        self.left = self.right = None
        
    def enqueue(self, val):
        if self.right:
            self.right.next = ListNode(val)
            self.right = self.right.next
        else:
            self.left = self.right = ListNode(val)
        
    def dequeue(self):
        if self.left:
            val = self.left.val
            self.left = self.left.next 
            return val
        else:
            print("Queue is empty already, nothing to deque!")
    
    def printQueue(self):
        curr = self.left 
        while curr:
            print(curr.val, "|", end = ' ')
            curr = curr.next 
        print()