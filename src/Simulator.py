from HashTable import HashTable
from Package import Package
from Location import Location
from DistanceGraph import DistanceGraph
from DistanceGraph import Vertex
from Dijkstras import Dijkstras
from Util import Util
class packageData:

    def __init__(self,pack,distance):
        self._package=pack
        self._distance=distance

#calculates shortest path and best distance for packages in each truck
class Simulator:
    def __init__(self, trucks, packageList,util):
        totalMiles=0
        boxTruck=[[],[],[]]
        index=0
        #Time Complexity: O(n^3) Space Complexity:O(n)
        for truck in trucks.table:
            package_queue=truck
            #set starting node for each truck as hub
            current_node="4001 South 700 East"
            route=""
            miles=0
            print "truck"
            #while there are still packages in the truck
            while(len(package_queue)>0):
                #creates new graph for each new node and runs it through Dijkstra's shortest path
                graph=util.loadDistance(DistanceGraph())
                vertex_a=graph.getKey(current_node)
                #Time Complexity: O(|V|^2) Space Complexity:O(|V|)
                d= Dijkstras(graph, vertex_a)
                #if last package set end_node as hub and calculate distance
                if(len(package_queue)==1):
                    vertex_b=graph.getKey("4001 South 700 East")
                    package_queue.pop()
                    rout=d.get_shortest_path(vertex_a,vertex_b)
                    shortest=vertex_b
                #find the shortest path to the next node
                else:
                    shortest=Vertex('')
                    pack_to_remove=None
                    #Time Complexity: O(n) Space Complexity:O(n)
                    for pack in package_queue:
                        vertex_b=graph.getKey(pack._address)
                        if(vertex_b.pred_node is not None):
                            rout=d.get_shortest_path(vertex_a,vertex_b)
                            if(vertex_b.distance<shortest.distance):
                                shortest=vertex_b
                                pack_to_remove=pack
                                route=rout
                    if pack_to_remove is not None:		
                        package_queue.remove(pack_to_remove)
                #set the current node as next location and print route data
                miles= miles+shortest.distance
                current_node=shortest.name
                #Time Complexity: O(n) Space Complexity:O(n)
                for package in packageList.table[0]:
                    if (package==pack_to_remove and len(package_queue)>=1):
                        boxTruck[index].append(packageData(package,shortest.distance))
                        print(vertex_a.name,shortest.name,shortest.distance, miles ,"Total Minutes to delivery: "+str((miles/18)*60) , package._deadline,package._notes)
                #print route data if last node is the hub
                if(len(package_queue)<1):
                    totalMiles=miles+totalMiles
                    boxTruck[index].append(packageData(package,shortest.distance))
                    print(vertex_a.name,shortest.name,shortest.distance,totalMiles)
                    self._totalMiles=totalMiles
                    
            index=index+1
        self._boxTrucks=boxTruck

    #simulates driving day and prints out status of packages at required times
    def simulate(self,PackageList,minut):
        packageList=PackageList.table[0]
        minutes=1
        #Time Complexity: O(n^3) Space Complexity:O(n)
        while( minutes<420):
            #truck 1 starts right away at 8:00 am
            #Time Complexity: O(n^2) Space Complexity:O(n)
            for pack in self._boxTrucks[0]:
                if ((pack._distance/16)*60 <=minutes):
                    self._boxTrucks[0].remove(pack)
                    #Time Complexity: O(n) Space Complexity:O(n)
                    for p in packageList:
                        if(p is pack._package):
                             p._deliveryStatus=True

            #truck 2 starts after 9:05
            if minutes>=65:
                    #Time Complexity: O(n^2) Space Complexity:O(n)
                for pack in self._boxTrucks[1]:
                    if ((pack._distance/18)*60 <=minutes):
                        self._boxTrucks[1].remove(pack)
                        #Time Complexity: O(n) Space Complexity:O(n)
                        for p in packageList:
                            if(p is pack._package):
                                p._deliveryStatus=True
            #truck 3 starts if first truck is empty
            if(len(self._boxTrucks[0])==0):
                for pack in self._boxTrucks[2]:
                       #Time Complexity: O(n^2) Space Complexity:O(n)
                    if ((pack._distance/16)*60 <=minutes):
                        self._boxTrucks[2].remove(pack)
                        #Time Complexity: O(n) Space Complexity:O(n)
                        for p in packageList:
                            if(p is pack._package):
                                 p._deliveryStatus=True
            minutes=minutes+1
            #print out status of packages during certain times
            if(minutes==minut):
                #Time Complexity: O(n) Space Complexity:O(n)
                for pack in packageList:
                    print pack._packageId,pack._address,pack._city,pack._state,pack._zipCode,pack._deadline,pack._weight,pack._notes,pack._deliveryStatus
                print (minutes, " -----------------------------")
        print("Total Miles: "+ str(self._totalMiles))
