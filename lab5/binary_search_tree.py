# final version for class notes

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, newkey):
        
        if self.root is None:			 # if tree is empty
            self.root = TreeNode(newkey)
            return
        else:
            p = self.root
            if p.key > newkey:
                if p.left is None:
                    p.left = TreeNode(newkey)
                else:
                    p.left.insert(newkey)
            else:
                if p.right is None:
                    p.right = TreeNode(newkey)
                else:
                    p.right.insert(newkey)

    def find (self, key):
        p = self.root      # current node
        while p is not None and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right

        if p is None :
            return False	    
        else:
            return True     # might want to return the node or ???

    def get(self,key,cnode):
        if not cnode:
            return None
        elif cnode.key == key:
            return cnode
        elif key < cnode.key :
            return self.get(key,cnode.left)
        else:
            return self.get(key,cnode.right)    

    def delete(self,key):
        if self.is_empty() == False :
            noderemove = self.get(key,self.root)
            if noderemove:
                 self.root.remove(noderemove)

         
    
    def print_tree(self):

        """   Print tree content inorder        """

        if (self.root.left != None):
            self.root.left.inorder_print_tree()

        print(self.root.key)

        if (self.root.right != None):
            self.root.right.inorder_print_tree()


    def is_empty(self):
        return self.root == None
     
   
    
class TreeNode:
    """Tree node: left and right child + data which can be any object"""

    def __init__(self,key,data=None,left=None,right=None, parent=None):

        self.key = key
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
    
    def hasleft(self):
        return self.left
    def hasright(self):
        return self.right
    def isleft(self):
        return self.parent and self.parent.left == self
    def isright(self):
        return self.parent and self.parent.right == self
    def isroot(self):
        return not self.parent
    def isleaf(self):
        return not (self.right or self.left)
    def has_any_child(self):
        return self.right or self.left
    def has_both_child(self):
        return self.right and self.left 
    def replaceNodeData(self,key,data,l,r):
        self.key = key
        self.data = data
        self.left = l
        self.right = r
        if self.hasleft():
            self.left.parent = self
        if self.hasright():
            self.right.parent = self


    def insert(self, key):
        """  Insert new node with key, assumes data not present """
        if self.key != None:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                   self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key
   
    def find_successor(self):
        suc = None
        if self.hasright():
    	    suc = self.right.find_min()
        else:
            if self.parent:
                if self.isleft():
                    suc = self.parent
                else:
                    self.parent.right = None
                    suc = self.parent.find_successor()
                    self.parent.right= self   
        return suc    
    
    def spliceout(self):
        if self.isleaf():
            if self.isleft():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_child():
            if self.hasleft ():
                if self.isleft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isleft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent







    def remove(self,currentNode):
        if currentNode.isleaf():
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.has_both_child():
            s = currentNode.find_successor()
            s.spliceout()
            currentNode.key = s.key
            currentNode.data = s.data
        else: # 1 child
            if currentNode.hasleft():
                if currentNode.isleft():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isright():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left


            else:
                if currentNode.isleft():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isright():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right



    def find_min(self):
        c = self
        while c.hasleft():
            c = c.left
        return c.key
     
    def find_max(self): 
        c = self
        while c.hasright():
           c = c.right
        return c.key

    def inorder_print_tree(self):
        if self.left is not None:
            self.left.inorder_print_tree()
        print(self.key)
        if self.right is not None:
           self.right.inorder_print_tree()     

    def print_level(self):
        if self == None:
            return []
        current = [self]
        result = []
        while current:
            level = []
            next = []
            for temp in current:
                level.append(temp.key)
                if temp.left:
                    next.append(temp.left)
                if temp.right:
                    next.append(temp.right)
            result.append(level)
            current = next
        return result



    
t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(10)
t.insert(1)
print ("Tree after inserting 8, 3, 10, 1")
t.print_tree()
print(t.root.find_max())
print(t.root.find_min())
t.root.inorder_print_tree()
t.insert(6)
t.insert(4)
print(t.is_empty())
print(t.root.find_successor())
t.insert(7)
t.insert(14)
t.insert(13)
t.delete(10)
print ("Tree after inserting 6, 4, 7, 14, 13")
t.print_tree()
print("Testing find 14")
print(t.find(14))
print("Testing find 15")
print(t.find(15))
print(t.root.print_level())
