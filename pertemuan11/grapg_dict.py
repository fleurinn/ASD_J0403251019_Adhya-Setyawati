class graph:
	#definisi graph
	def __init__(self, gdict=None):
		if gdict is None:
			gdict=[]
		self.gdict=gdict
		
	#mendapatkan vertex dari graph
	def getVertex(self):
		return list(self.gdict.keys())
		
	#mendapatkan egdes dari graph
	def getEdges(self):
		edges=[]
		for v in self.gdict:
			for e in self.gdict[v]:
				if {e,v} not in edges:
					edges.append({e,v})
		return edges
		
		
	#menambah vertex baru ke graph
	def addVertex(self,v):
		if v not in self.gdict:
			self.gdict[v]=[]
			
	#menambah edge baru ke graph
	def addEdge(self,e):
		(v1,v2)=e
		if v1 in self.gdict:
			self.gdict[v1].append(v2)
		else:
			self.gdict[v1]=[v2]
		if v2 in self.gdict:
			self.gdict[v2].append(v1)
		else:
			self.gdict[v2]=[v1]
			
# Create the dictionary with graph elements
graph1 = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

g=graph(graph1)
# Print the graph
print("awal",g.getVertex())
print("awal",g.getEdges())
g.addVertex("f")
print("tambah",g.getVertex())
g.addEdge({"f","a"})
print("tambah",g.getEdges())
g.addEdge({"f","g"})
print("tambah ke-2",g.getVertex())
print("tambah ke-2",g.getEdges())

