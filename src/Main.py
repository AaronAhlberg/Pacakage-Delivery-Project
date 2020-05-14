"""Aaron Ahlberg
   000986526
   c950
"""
from HashTable import HashTable
from Package import Package
from Location import Location
from DistanceGraph import DistanceGraph
from DistanceGraph import Vertex
from Dijkstras import Dijkstras
from Simulator import Simulator
from Util import Util
import csv
import os
#Prompt user for time after 8:00 am to get list of packages
minutes= input("Enter minutes after 8:00 am to retrieve status of packages: ")
#Util handles loading of data into graph and packageList
#Util class makes it easy to retrive and handle data in a single class
util=Util()
#loads packages into utils package list
util.loadPackageList()
#Assign variables to the data stored in utils
packageList=util._packageList
trucks=util._trucks
#Once data is all loaded the data can be manipulated and filtered to meet the requirements
#add and filter packages to certain trucks. 
#Time Complexity: O(1) Space Complexity:O(n)
trucks.insertInto(0,packageList.table[0][0])
trucks.insertInto(0,packageList.table[0][12])
trucks.insertInto(0,packageList.table[0][13])
trucks.insertInto(0,packageList.table[0][14])
trucks.insertInto(0,packageList.table[0][15])
trucks.insertInto(0,packageList.table[0][19])
trucks.insertInto(0,packageList.table[0][28])
trucks.insertInto(0,packageList.table[0][29])
trucks.insertInto(0,packageList.table[0][30])
trucks.insertInto(0,packageList.table[0][33])
trucks.insertInto(0,packageList.table[0][36])
trucks.insertInto(0,packageList.table[0][39])
#Truck 2
trucks.insertInto(1,packageList.table[0][2])
trucks.insertInto(1,packageList.table[0][5])
trucks.insertInto(1,packageList.table[0][17])
trucks.insertInto(1,packageList.table[0][24])
trucks.insertInto(1,packageList.table[0][35])
trucks.insertInto(1,packageList.table[0][37])
#Truck 3
trucks.insertInto(2,packageList.table[0][5])
trucks.insertInto(2,packageList.table[0][8])
trucks.insertInto(2,packageList.table[0][25])
trucks.insertInto(2,packageList.table[0][27])
trucks.insertInto(2,packageList.table[0][31])
count=0
#auto fill the rest of spots in trucks to size of 14 per truck
#Limiting the truck size to 14 packages improves delivery and total miles driven
#Time Complexity: O(n) Space Complexity:O(n)
for package in packageList.table[0]:
	#check if the amount of packages int truck is less than desired number
	if(len(trucks.table[count])<14):
		#add package into truck
		trucks.insertInto(count, package)
	#increment the counter to move to next truck and add more packages until table is empty
	else:
		count=count+1
		if(count<len(trucks.table)):
			trucks.insertInto(count, package)
#calculates shortest path for trucks and list of packages
sim = Simulator(trucks,packageList,util)
#simulates driving day and prints out status of packages at required times
sim.simulate(packageList,minutes)


		
		



	




	
		
	
		