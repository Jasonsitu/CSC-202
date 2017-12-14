class StackArray:
   """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

   def __init__(self, capacity):
      """Creates and empty stack with a capacity"""
      self.capacity = capacity
      self.items = [None]*capacity
      self.num_items = 0 

   def is_empty(self):
      """Returns true if the stack self is empty and false otherwise"""
      if self.size() == 0: 
         return True
      else:
         return False
   
   def is_full(self):
      """Returns true if the stack self is full and false otherwise"""
      return self.size() == self.capacity
   
   def push(self, item):
      if self.is_full():
         raise IndexError('The list is full')
      else:
         self.items[self.size()] = item #change the current index to item
         self.num_items += 1            # add a count
   def pop(self):
      """Returns item on the top of the stack and removes it"""
      if self.is_empty() == True:
         raise IndexError('The list is empty')
      else:
         x = self.items[self.size()-1] #give a name to the last item on the list
         self.num_items -= 1            # decrease the count
      return x                          # call that name
   def peek(self):
      """Returns item on the top of the stack but does not remove it"""
      return self.items[self.size()-1]  #return the last item on the list
   def size(self):
      """Returns the number of items in the stack"""
      return self.num_items             #return the length of the list

class Node:
   def __init__(self):
      self.head = None
      self.next = None      

class StackLinked:
   def __init__(self,capacity):
      self.top = 0
      self.root = Node()
      self.cap = capacity

   def is_empty(self):
      return self.top  == 0  #return true if length of stack is 0

   def is_full(self):
      return self.top == self.cap  #return true of capacity = length

   def push(self,item):            #if list is full, raise error 
      if self.is_full():
         raise IndexError()
      else:
         old = self.root            
         self.root = Node()    
         self.root.head = item   #add the item to the front
         self.root.next = old    #moving the old list behind
         self.top +=1            # add a count to keep track of length

   def pop(self):
      if self.is_empty():        #if list is empty raise error
         raise IndexError()
      else:
         x = self.root.head        #name the front of the list
         self.root = self.root.next  #move next > head
         self.top -= 1             #decrease a count
         return x                  #call the value we named 
   def peek(self):
      return self.root.head        #look at the top of the list

   def size(self):
      return self.top              # call the count 
