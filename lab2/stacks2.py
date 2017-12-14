class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity= capacity
        self.items = [None]*capacity
        self.num_items = 0 

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
 
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
 
    def push(self, item):
 
    def pop(self):
        """Returns item on the top of the stack and removes it"""
 
    def peek(self):
        """Returns item on the top of the stack but does not remove it"""

    def size(self):
       """Returns the number of items in the stack"""
 
