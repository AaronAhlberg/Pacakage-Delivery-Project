from DistanceGraph import DistanceGraph
from DistanceGraph import Vertex
class Dijkstras:
	#constructor takes the graph to be operated on and start node
	def __init__(self,graph, start_node):
		unvisited_nodes=[]
		#create list of unvisted nodes
		#Time Complexity: O(n) Space Complexity:O(n)
		for node in graph._graph_dict:
			unvisited_nodes.append(node)
		#set stat distance to 0
		start_node.distance=0
		start_node.pred_node=None
		#calculate shortest distance until out of unvisted nodes
		#Time Complexity: O(n^2) Space Complexity:O(n)
		while len(unvisited_nodes)>0:
			smallest=0
			#Finds the unvisted node with the smallest distance
			#Time Complexity: O(n) Space Complexity: O(n)
			for i in range(0, len(unvisited_nodes)):
				if unvisited_nodes[i].distance < unvisited_nodes[smallest].distance:
					smallest=i
			#Removes smallest node from unvisted queue
			current_node = unvisited_nodes.pop(smallest)
			#calculates alernate path distances between adjacent nodes
			#Time Complexity: O(n) Space Complexity:O(n)
			for adj_node in graph._graph_dict[current_node]:
				weight = graph._weights[(current_node,adj_node)]
				alt_path_distance = current_node.distance + float(weight)
			#If adjacent path is less than the current distance set new distance to current path
				if alt_path_distance<adj_node.distance:
					adj_node.distance=alt_path_distance
					adj_node.pred_node=current_node

	#returns shortest path between two nodes on graph
	def get_shortest_path(self,start_node,end_node):
		route=""
		current_node= end_node
		#loop backward to starting node to build route and calculate shortest path
		#Time Complexity: O(n) Space Complexity:O(n)
		while current_node is not start_node:
			route = ' -> ' + str(current_node.name) + route
			current_node = current_node.pred_node
		route = start_node.name + route
		#returns route of path
		return route