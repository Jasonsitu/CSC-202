
class HuffmanNode:
   def __init__(self, char, freq):
      self.char = char  # actually the character code
      self.freq = freq
      self.code = None
      self.left = None
      self.right = None

   def set_code(self, code):
      self.code = code

   def set_left(self, node):
      self.left = node

   def set_right(self, node):
      self.right = node

def comes_before(a, b):
   """returns true if tree rooted at node a comes before tree rooted at node b """
    
   if a.freq < b.freq:
      return True 
   elif a.freq == b.freq:
      if a.char < b.char:
         return True
      else:
         return False
   else:
      if a.freq > b.freq:
         return False  
   

def combine(a, b):
   """ creates a new huffman node with children a and b with combined freq with name of the left child """
   if a.freq < b.freq:
      temp = b
   elif a.freq == b.freq:
      if a.char < b.char:
         temp = a
      else:
         temp = b
   else:
      temp = a
   new_node = HuffmanNode(temp.char , a.freq + b.freq)
   return new_node
def cnt_freq(filename):
   file = open(filename)
   list = [0] * 256
   string = ""
   for i in file:
      string += i
   
   for x in string:
      list[ord(x)] += 1   
   return list
   file.close()
def create_huff_tree(list_of_freq):
   list = []
   for x,y in enumerate(list_of_freq):
      if y != 0:
         list.append(HuffmanNode(x,y))
   while len(list)> 1:
      a = find_min(list)
      list.remove(find_min(list))
      b = find_min(list)
      list.remove(find_min(list))
         
      new = combine(a,b)
      new.set_left(a)
      new.set_right(b)
      list.append(new)
   return list[0]
      
def find_min(list):
   min = list[0]
   for i in range(len(list)):
      if(comes_before(list[i],min)) == True :
         min = list[i]
   return min

def create_code (root_node,code = "",list = [""]*256):
    if root_node.left == None and root_node.right == None:
        list[root_node.char] = code
    else:
        if root_node.left != None:
            create_code(root_node.left,code = code + "0")
        if root_node.right != None:
            create_code(root_node.right, code = code + "1")
    return list

def tree_preord (root_node,code = ""):
    if root_node.right == None and root_node.left == None: 
        return "1" + str(root_node.char)
    else:
        if root_node.right != None:
            tree_preord(root_node.right, code = code + "0")
        if node.left != None:
            tree_preord(root_node.left, code = code + "1")
    return code
def huffman_encode(in_file, out_file):
    freq = cnt_freq(in_file)
    tree = create_huff_tree(freq)
    codelist = create_code(tree)
    inp_file = open(in_file,"r")
    output_file = open(out_file, "w")
    for i in inp_file.read():
        output_file.write(codelist[ord(i)])
    inp_file.close()
    output_file.close()
       


def huffman_decode(freqs, encoded_file, decode_file):
    tree = create_huff_tree(freqs)
    node = tree
    input_file = open(encoded_file, "r")
    output_file = open(decode_file, "w")
    code = ""
    for c in input_file.read():
        if c == "1":
            node = node.right
        elif c == "0":
            node = node.left
        if node.left == None and node.right == None: 
            code = code + chr(node.char)
            node = tree
        
    output_file.write(code)
    input_file.close()
    output_file.close()
