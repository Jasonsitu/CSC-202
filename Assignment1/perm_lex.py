def perm_gen_lex(a):
     
   if len(a) == 1:
      return [a]
   else:  
      list = []
      for x,y in enumerate(a):
         list += [y + p for p in perm_gen_lex(a[:x] + a[x+1:])]
      return list

     #   add the first character in the string and 
     #   then loop the rest of the character and add characters
     #   to the outer loop. x represent the index 
     #   while y represent the character in the string. 
