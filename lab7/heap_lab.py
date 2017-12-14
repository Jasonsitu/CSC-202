class MaxHeap:      #could not get the test case file to run...
   def __init__(self,capacity = 50):
   self.capacity = capacity
   self.heaplist = [0]+ ( [0] * capacity )
   self.size = 0   

   def is_empty():
      return self.size = 0

   def is_full():
      if self.size == self.capacity:
      	 return True
      else:
      	 return False

   def get_heap_cap():
      return self.capacity	

   def get_heap_size():
      return self.size

   def heap_contents(self):
      return self.heaplist


   def find_max():
      return self.heaplist[1]

   def del_max():
      x = self.heaplist[1]
      self.heaplist[1] = self.heaplist[self.size]
      self.size = self.size - 1
      self.heaplist.pop()
      self.percDown(1)
      return x


   def perc_up(self, i):
      while i // 2 > 0:
         if self.heapList[i] > self.heaplist[i//2]:
            temp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[i//2]
            self.heaplist[i//2] = temp
         i = i // 2
   def perc_down(self,i): 
      while (i * 2) <= self.size:
         mc = self.maxChild(i) 
         if self.heaplist[i] < self.heaplist[mc]: #if parent < maxchild then swap
            tmp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[mc]
            self.heaplist[mc] = tmp
         i = mc
    def maxChild(self,i):
       if i * 2 + 1 > self.size:
           return i * 2
       else:
           if self.heaplist[i*2] > self.heaplist[i*2+1]:
               return i * 2
           else:
               return i * 2 + 1


   def insert(self,item):
      if self.is_full():
         return False
      else:
         self.heaplist.insert(1,item)
         self.size = self.size + 1
         self.perc_down(1)
         return True


   def build_heap(self,alist):
      if self.capacity < len(alist) - 1:
         return False
      else:
         i = len(alist) // 2
         self.size = len(alist)
         self.heaplist = [0] + alist[:]
          while i > 0 : 
             self.perc_down(i)
             i = i - 1
          return True
   
    def heap_sort_increase(self,alist):
       self.build_heap(alist)
       while self.size > 1:
          temp = self.heaplist[self.size]
          self.heaplist[self.size] = self.heaplist[1]
          self.heaplist[1] = temp
          self.size = self.size - 1
          self.perc_down(1)
       return self.heaplist

   
