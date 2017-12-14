class Node:
   def __init__(self,data):
      self.data = data
      self.next = None
      self.prev = None
   
   def getData(self):
      return self.data
   
   def getNext(self):
      return self.next

   def getPrev(self):
       return self.prev
   
   def setData(self,newdata):
      self.data = newdata
   
   def setNext(self,newnext):
      self.next = newnext
    
   def setPrev(self,newprev):
      self.prev = newprev
class OrderedList():

   def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0
    
   def add(self,item):
      new = Node(item)
      if self.head is None:
         self.head = new
      elif self.head.data > new.data:
         new.setNext(self.head)
         self.head.setPrev(new)
         self.head = new
      else:
         prev = self.head
         c = self.head.next
         while c is not None:
            if cur.data > new.data:
               prev.setNex(new)
               new.setPrev(prev)
               new.setNext(c)
               c.setPrev(new)
            prev = c
            c = c.next
            

   def remove(self,item):
      current = self.head
      previous = None
      found = False
      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
          self.head = current.getNext()
      else:
          previous.setNext(current.getNext())
    
   def search_forward(self,item):
      current = self.head
      while current != None:
         if current.getData() == item:
            return True
         elif current.getData() > item:
            return False
         current = current.getNext()
      return False
 
   def search_backward(self,item): #pass
  
   
   def is_empty():
      return self.head == None:
          
   def size(self):    
      current = self.head
      count = 0
      while current != None:
          count = count + 1
          current = current.getNext()
      return count
   
   def index(item):
      current = self.head
      i = 0
      while current != None:
         if current.getData() == item:
            return i
         i += 1
         current = current.getNext()
      return i 
      
     
   def pop():
      if self.size() == 0:
         Raise ValueError("List is empty")
      else:
         temp = self.head.getPrev()
         new = temp.getPrev()
         self.head.setPrev()
         new.setNext(None)
      return temp.getData()
       

    
   def pop(pos):  #imcomplete
      if self.is_empty() == True:
         raise ValueError("List is empty")
      
      elif pos <= self.size() -1 :
         prev = self.head
         current = prev.getNext()
         if pos is None:
            while current is not None:
               if current.next is None:
                  prev.setNext(None)
               prev = current
               current = current.next
            self.head = None
            return prev
         

    










