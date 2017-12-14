class MyGraph:
	def __init__ (self, filename): 
	    file = open(filename, "r")
	    self.ad_list = []
	    line = file.readlines()
	    pair = (1,[])
	    self.vert = int(line[0])
	    self.edge = int(line[1])

	    for x in range(self.vert):
	    	pair = (i + 1 ,[])
	    	self.ad_list.append(pair)
	    for x in range(2, self.edge + 2):
	    	split = line[x].split()
	    	a = int(split[0]) - 1 
	    	b = int(split[1]) - 1
	    	self.ad_list[f][1].append(split[0])
	    	self.ad_list[f][1].append(split[0])

	    for x in range(self.vert):
	    	self.ad_list[i][1].sort()

	def conn_components(self):
		components = []
		temp = []
		visit = []
		for x in range(self.vert):
			if x not in visit:
				temp = []
				self.depth(x,visit,temp)
				components.append(temp)
		return components

	def depth(self,node,visit,temp):
		if node not in  visit:
			visit.append(node)
			temp.append(node)
			for x in range(len(self.ad_list[node][1])):
				print("test")
				print(self.ad_list[node][1])
				self.depth(int(self.ad_list[node][1][x]),visit,temp)
	def bicolor(self):
		pass

	


