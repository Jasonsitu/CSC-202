class QueueArray:
   def __init__(self,capacity):
      self.capacity = capacity
      self.queue = [0] * capacity
      self.size= 0
      self.front = 0
      self.rear= 0
 
   def is_empty(self):
      return self.size == 0    #return true if size equal 0

   def is_full(self):
      return self.size == self.capacity  # return true of size equal the capacity
   
   def enqueue(self,item):        # raise error if capacity is met
      if self.is_full() == True:
         raise IndexError("Queue is Full")   
      else:
         self.queue[self.rear] = item     # set the last index as item
         self.rear = (self.rear + 1) % self.capacity 
         self.size += 1                 # increase count by 1

   def dequeue(self):
      if self.is_empty():
         raise IndexError("Queue is empty")    #raise error if queue is empty
      else:
         p = self.queue[self.front]             # set a name for the front index
         self.front = (self.front + 1) % self.capacity  
         self.size -= 1        #decrease count by 1
         return p

   def num_in_queue(self):
      return self.size      #return the length of the queue


class Node(object):
   def __init__(self,head=None):
      self.head = head
      self.next = None

class QueueLinked:
   def __init__(self,capacity):
      self.count = 0
      self.first = None
      self.last = None
      self.cap = capacity

   def is_empty(self):
      return self.count == 0  # return true if length of queue is zero
 
   def is_full(self):
      return self.count == self.cap  # return true if length equal capacity

   def enqueue(self,item):
      new = Node(item)         #make a new node with item as the head
      new.next = None          
      if self.first == None:      #if there isnt a node
         self.first = self.last =new     #set the first node as the new node
      else:
         l = self.last     #find the last node
         l.next = new      # append the new node
         self.last = new
      self.count += 1       # increase the count each time its run


   def dequeue(self):
      if self.is_empty():     #raise error if the queue is empty
         raise IndexError()
      else: 
         p = self.first.head    #give a name for the first node
         self.first = self.first.next  #set the next node as the first node
         self.count -= 1        #decrease the count by 1
         return p 
      

   def num_in_queue(self):
      return self.count           #return the length of the queue
 
      


















