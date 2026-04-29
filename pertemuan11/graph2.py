class graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdict=[]
		self.gdict=gdict
				
	#menambahkan sebuah vertex pada graph
	#vertex sebagai key/kunci pada dictionary
	def addVertex(self,v):
		if v not in self.gdict:
			self.gdict[v]=[]
	
	def addEdge(self, e):
		(v1,v2)=e 
		print ('v1',v1)
		print ('v2',v2)
		if v1 in self.gdict: #jika v1 sudah ada di graph
			self.gdict[v1].append(v2) #menambahkan v2 dalam valuenya v1
		else: #jika v1 blum ada di graph
			self.gdict[v1]=[v2] #jadikan v1 key, v2 value
		if v2 in self.gdict:
			self.gdict[v2].append(v1)	
		else:
			self.gdict[v2]=[v1]		
			
				
	#mendapatkan vertex dari graph
	def getVertex(self):
		return list(self.gdict.keys())
	#menambahkan edge pada graph		
	#menemukan setiap edge dari graph
	def findEdge(self):
		edge=[]
		for v in self.gdict:
			#print("v",v)
			for e in self.gdict[v]:
				#print ("e",e)
				if {e,v} not in edge:
					edge.append({v,e})
					#print("edge",edge)
		return edge


# Create the dictionary with graph elements
graph1 = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

g=graph(graph1)
#g.addVertex("f")
g.addEdge(('A','a'))
#g.addEdge({'a','c'})
# Print the graph 		 
print("edge",g.findEdge())
print("vertex",g.getVertex())
