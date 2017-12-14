from stacks import StackArray

def infix_to_postfix(infixexpr):
   """Converts an infix expression to an equivalent postfix expression """

   """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    
   s = StackArray(30)
   postfixList = []
   tokenList = infixexpr.split()
   prec = {'^':4, '/':3, '*':3, '+':2, '-':2, '(':1}
   for t in tokenList:
      if t in "0123456789":
         postfixList.append(t)
      elif t == "(":
         s.push(t)
      elif t ==")":
         topt = s.pop()
         while topt != "(":
            postfixList.append(topt)
            topt = s.pop()
      else:
         while (not s.is_empty()) and \
            (prec[s.peek()] >= prec[t]):
               postfixList.append(s.pop())
         s.push(t)

   while not s.is_empty():
      postfixList.append(s.pop())
   return " ".join(postfixList)


def postfix_eval(postfixExpr):
   """  Purpose """

   s = StackArray(30)
   token = postfixExpr.split()

   for t in token:
      if t in "0123456789":   #if the string character is in that string
         s.push(int(t))       # convent that string character into an integer
      else:
         op1 = s.pop()        #pop the first two integer
         op2 = s.pop()
         result = doMath(t,op1,op2)   # give a value for  the operation
         if result == "ValueError": #check if it is dividing by 0 if so raise an Error 
            raise ValueError("Value Error")
         else:
            s.push(result)    #else add the result to the stack
   return s.pop() #return the value after it loops through all the operators


def doMath(op, op1, op2):
   """  Purpose """
   if op == "^":    
      return op1 ** op2
   elif op == "*":
      return op1 * op2
   elif op == "/":    #if the operator is / check if any of the operand is 0, if not 
      if op1 ==0:    #then continue to do the operation
         return "ValueError"
      else:
         return op1 / op2
   elif op == "+":
      return op1 + op2
   else:
      return op1 - op2
   
def postfix_valid(postfixexpr):
   """ Purpose """
   s = StackArray(30)
   count = 0
   count2 = 0
   tokenList = postfixexpr.split()
   prec = {'^':4, '/':3, '*':3, '+':2, '-':2, '(':1}
   for t in tokenList:        #made two counters, one for operators and and operands
      if t in "0123456789":   #the only way its a valid expression if the total of
         count += 1           # operator + 1 = operands, 
      else:
         count2 += 1
   if count == (count2 + 1):
      return True
   else:
      return False
         




