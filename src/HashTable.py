bucket_list=list()

class HashTable:

	def __init__(self,	size=1):
		self.table=[]
		#splits data into number of buckets table was initialised with. 
		for i in range(size):
				self.table.append([])

	#inserts a package object into the hash table
	#Time Complexity: O(1) Space Complexity:O(n)
	def insert(self,package):
		self.table[package._packageId%len(self.table)].append(package)
    
	#loops through Hashtable and returns package object that matches
	#Time Complexity: O(1) Space Complexity:O(n)
	def search(self,package):
		for row in self.table:
			for item in row:
				if(item == package):
					return True
		return False		

	#Inserts package into specific bucket after search
	#Time Complexity: O(1) Space Complexity:O(n)
	def insertInto(self, bucketId, package):
		if self.search(package) is False:
			self.table[bucketId].append(package)
	
	
		