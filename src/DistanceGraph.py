class Vertex:
	def __init__(self, name):
		self.name = name
		self.distance = float ('inf') 
		self.pred_node= None
class DistanceGraph:
	def __init__(self):

		self._graph_dict={}
		self._weights={}
	#Time Complexity: O(1) Space Complexity:O(n)
	def add_node(self, node):
		if node not in self._graph_dict:
			self._graph_dict[node]= []
	#Time Complexity: O(1) Space Complexity:O(n)
	def add_directedEdge(self, start_node, end_node, weight=1.0):
		self._weights[(start_node,end_node)]=weight
		self._graph_dict[start_node].append(end_node)
	
	#adds a directed edge between A->B and B->A
	#Time Complexity: O(1) Space Complexity:O(n)
	def add_undirectedEdge(self, start_node, end_node, weight=1.0):
		self.add_directedEdge(start_node,end_node,weight)
		self.add_directedEdge(end_node,start_node,weight)
	#returns the key for the vertex instance in the graph dictionary. Used as a workaround to not lose reference to vertex object instance
	#during data manipulation. 
	#Time Complexity: O(n) Space Complexity:O(n)
	def getKey(self, name):
		for key in self._graph_dict.keys():
			if(key.name==name):
				return key
			
    	