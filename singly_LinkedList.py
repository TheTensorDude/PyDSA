# Node of a LinkedList
# val represents the value inside the node 
# next is a reference pointer to the next ListNode 
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class SinglyLinkedList:
    """
    Constructs a Singly Linked List, where each node in the linked list
    points to the next node if exists else points to None/Null.
    """
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head 
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        
    def removeIndex(self, index):
        count = 0
        curr = self.head    
        while count < index and curr:
            curr = curr.next 
            count += 1
            
        if curr:
            curr.next = curr.next.next
        else:
            print("Index does not exist in the Linked List")
            
    def printList(self):
        curr = self.head.next
        while curr:
            print(curr.val, ' -> ',  end=' ')
            curr = curr.next
        print()