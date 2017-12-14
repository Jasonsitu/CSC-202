class MyHashTable:
    def __init__(self, table_size = 11):
        self.table_size = table_size
        self.size = 0
        self.collisions = 0
        self.hash_table = [[]for x in range(self.table_size)]

    def insert(self,key,item):
        value = self.hashfunction(key,self.table_size)
        new_item = (key, item)
        if len(self.hash_table[value]) == 0:
            self.hash_table[value].append(new_item)
            self.size = self.size + 1
        else:
            x = 0
            found = False
            while x < len(self.hash_table[value]) and not found:
                if self.hash_table[value][x][0] == key:
                    self.hash_table[value][x] = new_item
                    found = True
                else:
                    self.hash_table[value].append(new_item)
                    x = x + 1
            self.size = self.size + 1
            self.collisions = self.collisions + 1
        if self.load_factor() > 1.5: 
            self.rehash()

    def remove(self,key):
        found = False
        value = self.hashfunction(key,self.table_size)
        x = 0
        item = None
        if len(self.hash_table[value]) == 0:
            raise LookupError("key does not exist")
        else:
            while x < len(self.hash_table[value]) and not found:
                if self.hash_table[value][x][0] == key:
                    item = self.hash_table[value].pop(x)
                    self.size = self.size - 1
                    found = True
                else:
                    x += 1
        if item == None:
            raise LookupError("key does not exist")
        else:
            return item 

    def rehash(self):
        new_size = (self.table_size * 2) + 1
        new_table = [[] for x in range(new_size)]
        for x in range(self.table_size):
            for x in self.hash_table[x]:
                value = self.hashfunction(x[0],new_size)
                new_table[value].insert(0,x)
        self.table_size = new_size
        self.hash_table = new_table
    def get(self,key):
        found = False
        value = self.hashfunction(key,self.table_size)
        x = 0
        item = None
        if len(self.hash_table[value]) == 0:
            raise LookupError("key does not exist")
        else:
            while x < len(self.hash_table[value]) and not found:
                if self.hash_table[value][x][0] == key:
                    item = self.hash_table[value][x]
                    found = True
                else:
                    x += 1
        if item == None:
            raise LookupError("key does not exist")
        else:
            return item
    

    def get_size(self):
        return self.size
    
    def load_factor(self):
        load = self.size / self.table_size
        return load

    def get_collisions(self):
        return self.collisions

    def hashfunction(self,key,size):
        return key % size
