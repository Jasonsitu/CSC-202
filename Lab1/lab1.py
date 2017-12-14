def max_list_iter(tlist):  # must use iteration not recursion
   """ finds the max of a list of numbers and returns it, not the index"""
   max = 0
   for i in tlist:
     if max < i:
        max = i
     return max
   else:
      raise ValueError('empty list')
   

def reverse_rec(tempstr):   #must use recursion
   """ recursively reverses the characters in a string """
   if tempstr == "":
      return tempstr
   else: 
      return reverse_rec(tempstr[1:]) + tempstr[0]


def bin_search(target, low, high, list_val):  #must use recursion
   """ searches for target in list_val[low..high] and returns index if found"""
   mid = (low + high) // 2
   if list_val == []:
      return None
   elif target not in list_val:
      return None
   elif target == list_val[mid]:
      index = mid
   elif target < list_val[mid]:
      index = bin_search(target, low, mid - 1, list_val)
   elif target > list_val[mid]:
      index = bin_search(target, high , mid + 1 ,list_val)
   else: 
      return None
   return index
