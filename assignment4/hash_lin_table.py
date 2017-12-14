class HashTableLinPr:
    def __init__(self,table_size = 251):
        self.table_size = table_size
        self.hash_table = [None] * self.table_size
        self.stop_table_size = table_size
        self.words_list = []
        self.stop_list = []
        self.stop_table = [None] * self.stop_table_size
    def hash(string,self):
        count = 0
        value = self.myhash(string,self.stop_table_size) + count
        while(self.stop_table[value] != None):
            count = count + 1
            if(self.myhash(string,self.stop_table_size) + count > self.stop_table_size -1):
                value = self.myhash(string,self.stop_table_size) + count % self.stop_table_size
            else:
                value = self.myhash(string,self.stop_table_size) + count
        return value
    def rehash(self):
        new_size = (self.stop_table_size * 2) + 1
        new_table = [None] * new_size
        for i in self.stop_list:
            hash_value = self.myhash(i, new_size)
            count = 0
            while(new_table[hash_value] != None):
                count = count + 1
                if(self.myhash(i,new_size) + count > new_size):
                    hash_value = (self.myhash(i,new_size) + count) % new_size
                else:
                    hash_value = self.myhash(i,new_size) + count
            new_table[hash_value] = i
        self.stop_table_size = new_size
        self.stop_table = new_table

    def contains(self,key):
        lkey = key.lower()
        index = self.myhash(key,self.stop_table_size)
        containing = False
        for x in self.stop_list:
            if x == key:
                containing = True
        while(self.stop_table[index] != None):
            if(self.stop_tablep[index] == lkey):
                containing = True
            else:
                index = index + 1
        return containing

    def read_stop(self,filename):
        file = open(filename, "r")
        line = f.readline()
        if(line[len(line)-1] == "\n"):
            line = line[:len(line)-1]
        while line:
            line = line.lower()
            index = 0
            pun = False
            for x in range(len(line)-1):
                if(ord(line[x])==45):
                    index = x
                    pun = True
            if(not pun):
                count = 0
                for i in range(len(line)-1):
                    if line[i] == "'":
                        line = line[:i]+ line[i+1:]
                hash_value = self.hash(line)
                self.stop_table[hash_value] = line
                self.stop_list.append(line)

            else:
                beg = line[:index]
                last = line[index+1:]
                hash_value = self.hash(beg)
                for pos in range(len(beg) - 1):
                    if beg[pos] == "'":
                        beg = beg[:pos] + beg[pos+1:]
                self.stop_list.append(beg)
                self.stop_table[hash_value] = beg
                count = 0
                hash_value = self.hash(last)
                for pos in range(len(last) - 1):
                    if last[pos] == "'":
                        last = last[:pos] + last[pos+1:]
                self.stop_list.append(last)
                self.stop_table[hash_value] = last
            if(self.get_load_fact_stop() > .5):
                self.rehash()
            line = file.readline
        file.close()
        
    def read_file(self,filename,stop_table):
        num = 1
        file = open(filename,"r")
        line =file.readline()
        while line:
            word = ""
            line = line.lower()
            if(line[len(line)-1] == '\n'):
                line = line[:len(line)-1]
            for i in range(len(line)):
                value = ord(line[i])
                if(value >= 65 and value <=122):
                    word = word + line[i]
                else:
                    if(len(word) > 0):
                        index = self.myhash(word,len(self.stop_list))
                        search_index = index
                        if(not self.contains(word)):
                            self.add(word,num)
                        word = ""
            if(len(word) > 0):
                if(not self.contains(word)):
                    self.add(word,num)
            line = f.readline()
            num = num + 1
        file.close()
    def add(self,key,line):
        if(self.get_load_fact()>.5):
            new_size = self.table_size * 2 + 1
            new_table = [None] * new_size
            for x in words_list:
                index = self.myhash(x,new_size)
                count = 1
                while(self.hash_table[index] != x):
                    index = index + 1
                item = self.hash_value[index]
                new_index = self.myhash(item[0], self.table_size)
                insert_index = new_index
                while(new_table[insert_index]) != None:
                    insert_index = new_index + count
                    count = count + 1
                new_table[insert_index] = item
            self.hash_table = new_table
        index = self.myhash(key,self.table_size)
        duplicate = False
        while(self.hash_table[index] != None and not duplicate):
            if(self.hash_table[index][0] == key):
                lines = self.hash_table[index][1]
                if(lines[len(lines)-1] != line):
                    self.hash_table[search_index][1].append(line)
                duplicate = True
            else:
                index = index + 1
        if(not duplicate):
            self.hash_table[index] = (key,[line])
            self.words_list.append(key)
  
    def save_concordance(self,outputfilename):
        list_of_items = []
        for x in range(self.table_size):
            if(self.hash_table[x] != None):
                list_of_items.append(self.hash_table[x])
        sort_list = sorted(list_of_items,key = lambda list_of_items:list_of_items[0])
        file = open(outputfilename,'w')
        for i in range(len(sort_list)-1)
            write = sort_list[i][0] + ': '
            for j in range(len(sort_list[i][1])):
                write = write + str(sort_list[i][1][j]) + " "
            file.write(write + '\n')
        f.close()
     
    def myhash(self,key,table_size):
        value = 0
        num = min(len(key),8)
        for i in range(num):
            value = (value * 31) + ord(key[i])
        return value
    def get_load_fact_stop(self):
        return len(self.stop_list) / self.stop_table_size
    def get_load_fact(self):
        load = len(self.words_list)/self.table_size
        return load
    def get_tablesize(self):
        return len(self.hash_table)


