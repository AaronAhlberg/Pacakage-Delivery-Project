from HashTable import HashTable
from Package import Package
from Location import Location
from DistanceGraph import DistanceGraph
from DistanceGraph import Vertex
from Dijkstras import Dijkstras
import csv
import os
class Util:

    #Sets default directory to users desktop
    #assing variables to default values
    def __init__(self):
        os.chdir(r'C:\Users\Aaron\Desktop') 
        self._graph=DistanceGraph()
        self._packageList=HashTable(1)
        self._locationQueue=[]
        #Creates a bucket in the hash table for each truck 
        self._trucks=HashTable(3)

    
    def loadPackageList(self):
        #reads package data from file and creates a package object to be passed to the hash table
        #create file reader with ',' as delimiter
        with open('WGUPS Package File.csv') as file:
            fileReader = csv.reader(file , delimiter=",")
            #for each row in file reader create a new package object and adds it to _packageList
            #Time Complexity: O(n) Space Complexity:O(n)
            for row in fileReader:
                self._packageList.insert(Package(int(row[0]),row[1],row[2],row[3],row[4],row[5],row[6],row[7]))


    #reads in distance data and adds nodes to the graph. Since the the graph does not map the nodes
    # in sequence a list is used to hold location information for later use when adding edges to the graph. 
    def loadDistance(self,graph):
        locationQueue=[]
        #open file and create file reader with a delimiter of ","
        with open('DistanceTable.csv') as file:
            fileReader =csv.reader(file, delimiter=",")
            #Time Complexity: O(n) Space Complexity:O(n)
            for row in fileReader:
                #Clean data in file by removing \n in csv file
                row[0]=row[0].replace("\n","")
                row[1]=row[1].replace("\n","")
                #create location object and add it to list
                location = Location(row[0],row[1],row[2:])
                locationQueue.append(location)
                # add a vertex to the graph using the location address
                vert= Vertex(location._address)
                graph.add_node(vert)
                

    #adds all distance data to graph from bidirectional matrix
    # A locationQueue was needed to keep an ordered set of addresses to loop through. 
    # HashTable does not keep the address ordered and makes it inconsistent to loop through
        count = 0
        #Time Complexity: O(n^3) Space Complexity:O(n)
        while (count<len(locationQueue)):
            for location in locationQueue: #For each location in list
                if location._distances[count] is not '': #Adds distance data that is not left blank
                    for key in graph._graph_dict.keys(): #retireves keys from dictionary in graph
                        if(key.name== location._address):#check to see if the location matches
                            vert_a=key
                        if(key.name==locationQueue[count]._address): 
                            vert_b=key 
                    #Adds vertexes to graph. Since graph is undirected only half of the matrix needs to be scanned in
                    graph.add_undirectedEdge(vert_b,vert_a,location._distances[count])
            count=count+1
        #returns the altered graph and stores it for later reference
        self._graph=graph
        return graph