def insert_sort(alist):
   count = 0 
   for index in range(1,len(alist)):
      current = alist[index]
      position = index
      count += 1
      while position > 0 and alist[position-1] > current:
         alist[position] = alist[position-1]
         position = position -1
      alist[position] = position - 1
   print count




def select_sort(alist):
   count = 0
   for f in range(len(alist)-1, 0 , -1):
      pos_max = 0
      for location in range(1,f +1 ):
         count += 1
         if alist[location] > alist[pos_max]:
             pos_max = location
      temp = alist[f]
      alist[f] = alist[pos_max]
      alist[pos_max] = temp
   print count
def merge_sort(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       merge_sort(lefthalf)
       merge_sort(righthalf)

       i=0
       j=0
       k=0
       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
    

alist = [54,26,93,17,77] # made a graph that went up by size 5 each time 
merge_sort(alist)
print(alist)
insert_sort(alist)
select_sort(alist)
blist = [54,26,93,17,77,31,44,55,20,5]
merge_sort(blist)
print(blist)
insert_sort(blist)
select_sort(blist)
clist = [54,26,93,17,77,31,44,55,20,5,25,9,11,99,90]
merge_sort(clist)
print(clist)
insert_sort(clist)
select_sort(clist)
dlist = [54,26,93,17,77,31,44,55,20,5,25,9,11,99,90,3,21,55,33,22] #worst case because none of them list is in order. 
merge_sort(dlist)
print(dlist)
insert_sort(dlist)
select_sort(dlist)
elist = [1,1,1,1]
insert_sort(elist)
select_sort(elist)
