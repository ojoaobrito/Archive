#!/usr/bin/env python
# encoding: utf8
# Artificial Intelligence, UBI 2018-19
# Modified by: Nuno Salvado (a37575) and João Brito (a37880)

import time
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

dictionary = {} # dictionary with every object category observed so far (except for people)
people = [] # list that contains every person in the world, as well as the room they are in (ex: ["Mary",3])

rooms = [[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],[0,[]]] # dictionary with the inventory of objects in each room

# variables that give information about the robot's position in the world
current_global = 0
visited = [current_global]
start_global = 0
room_ant = 1
x_ant = 0.0
y_ant = 0.0
obj_ant = ''
movement = 0 # 1 if the robot starts moving within the room is in, 0 if he has just arrived

# variables for question 6
graph = [[],[],[],[],[],[],[],[],[],[],[],] # graph that represents the world
paths = []
aux = [current_global]

# room coordinates ([(...), [room1_x_axis, room1_y_axis], (...)])
room_coordinates = [[[-0.9,3.6],[-3.1,1.5]],[[-0.9,3.6],[1.6,6.5]],[[-0.9,3.6],[6.6,11.1]],[[-6.0,-1.0],[-3.1,1.5]],[[-6.0,1.0],[1.6,11.1]],[[-11.0,-6.1],[-3.1,1.5]],[[-11.0,-6.3],[1.6,6.5]],[[-11.0,-6.1],[6.6,11.1]],[[-15.6,-11.1],[-3.1,1.5]],[[-15.6,-11.1],[1.6,6.5]],[[-15.6,-11.1],[6.6,11.1]]]

# room types
waiting_room = {"chair"}
study_room = {"chair", "table", "book"}
computer_lab = {"computer", "chair", "table"}
meeting_room = {"chair", "table"}

time_room = 0.0
times = [[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0],[0,0.0]]

# ------------------------------------------------------------------------------------------------------
# AUXILIARY FUNCTION - returns the room where the robot is in, at any given point in time - DONE BY João
def robot_room():
	
	global x_ant, y_ant, room_coordinates
	
	if(x_ant>=room_coordinates[0][0][0] and x_ant<=room_coordinates[0][0][1] and y_ant>=room_coordinates[0][1][0] and y_ant<=room_coordinates[0][1][1]):
		return 1
		
	if(x_ant>=room_coordinates[1][0][0] and x_ant<=room_coordinates[1][0][1] and y_ant>=room_coordinates[1][1][0] and y_ant<=room_coordinates[1][1][1]):
		return 2
		
	if(x_ant>=room_coordinates[2][0][0] and x_ant<=room_coordinates[2][0][1] and y_ant>=room_coordinates[2][1][0] and y_ant<=room_coordinates[2][1][1]):
		return 3
		
	if(x_ant>=room_coordinates[3][0][0] and x_ant<=room_coordinates[3][0][1] and y_ant>=room_coordinates[3][1][0] and y_ant<=room_coordinates[3][1][1]):
		return 4
		
	if(x_ant>=room_coordinates[4][0][0] and x_ant<=room_coordinates[4][0][1] and y_ant>=room_coordinates[4][1][0] and y_ant<=room_coordinates[4][1][1]):
		return 5
		
	if(x_ant>=room_coordinates[5][0][0] and x_ant<=room_coordinates[5][0][1] and y_ant>=room_coordinates[5][1][0] and y_ant<=room_coordinates[5][1][1]):
		return 6
		
	if(x_ant>=room_coordinates[6][0][0] and x_ant<=room_coordinates[6][0][1] and y_ant>=room_coordinates[6][1][0] and y_ant<=room_coordinates[6][1][1]):
		return 7
		
	if(x_ant>=room_coordinates[7][0][0] and x_ant<=room_coordinates[7][0][1] and y_ant>=room_coordinates[7][1][0] and y_ant<=room_coordinates[7][1][1]):
		return 8
		
	if(x_ant>=room_coordinates[8][0][0] and x_ant<=room_coordinates[8][0][1] and y_ant>=room_coordinates[8][1][0] and y_ant<=room_coordinates[8][1][1]):
		return 9
		
	if(x_ant>=room_coordinates[9][0][0] and x_ant<=room_coordinates[9][0][1] and y_ant>=room_coordinates[9][1][0] and y_ant<=room_coordinates[9][1][1]):
		return 10
		
	if(x_ant>=room_coordinates[10][0][0] and x_ant<=room_coordinates[10][0][1] and y_ant>=room_coordinates[10][1][0] and y_ant<=room_coordinates[10][1][1]):
		return 11
	
# ----------------------------------------------------------------------------------------------
# QUESTION 1 ("How many different types of objects did you recognize until now?") - DONE BY Nuno
def objects_recognized():
	
	global dictionary, people
	
	count = 0
	count2 = 0
	
	count = len(dictionary)
	count2 = len(people)
	
	if(count==1 and count2==0):
		print "\n> So far, I have seen 1 type of object and no people\n"
	
	elif(count==1 and count2==1):
		print "\n> So far, I have seen 1 type of object and 1 person\n"
	
	elif(count==1 and count2>1):
		print "\n> So far, I have seen 1 type of object and " + str(count2) + " people\n"
	
	elif(count2==1):
		print "\n> So far, I have seen " + str(count) + " types of objects and 1 person\n"
	
	else:
		print "\n> So far, I have seen " + str(count) + " types of objects and " + str(count2) + " people\n"

# -----------------------------------------------------------------------------------------
# QUESTION 2 ("Which objects were in the room you visited before this one?") - DONE BY João
def objects_in_previous_room():
	
	global room_ant, rooms
	
	length = 0
	final = ""
	
	for i in rooms[room_ant-1][1]:
		if(length==(len(rooms[room_ant-1][1])-2)): # the second to bottom item
			final = final + i + " and "
		
		elif(length==(len(rooms[room_ant-1][1])-1)): # the last item
			final = final + i
		
		else: # the remaining items
			final = final + i + ", "
		
		length += 1
	
	if(length==0):
		print "\n> In the previous room (" + str(room_ant) + ") I found nothing\n"	
	
	else:
		print "\n> The previous room (" + str(room_ant) + ") had this: " + final + "\n"
		
# -------------------------------------------------------------------------
# QUESTION 3 ("What is the probability of finding 10 books in this world?") DONE - BY Nuno
def ten_books():
	
	global dictionary, people
	total = 0
	books = 0
	
	for i,j in dictionary.items():
		if(i=="book"):
			books = j
		total += j
	
	total += len(people)
	
	if(total==0):
		print "\n> I reckon there's 0.0% chance of that happening...\n"
		return
	
	print "\n> I reckon there's %.3f%% chance of that happening\n" % (((float(books)/total)**(10-books))*100.0)

# ----------------------------------------------------------------------------------------------------------------------------
# QUESTION 4 ("What type of object do you think is the one whitout identification, that appears close to Joe?") - DONE BY João
def object_joe():
	
	global dictionary, people, waiting_room, study_room, meeting_room, computer_lab
	
	room_types = [waiting_room,study_room,computer_lab,meeting_room]
	maximum = ["chair",0] # most common object so far (name and quantity, by default it's a chair)
	room_type_temp = []
	joes_objects = set()
	room_types_objects = set()
	aux = set()
	
	for i in people:
		if(i[0]=="joe"):
			
			# we have only seen Joe in his room
			if(len(rooms[i[1]-1][1])==1 and i[0] in rooms[i[1]-1]):
				
				# our best guess is that the unidentified object is the most common one so far
				for j,k in dictionary.items():
					if(k>maximum[1]):
						maximum = [j,k]
				print "\n> Not enough information, but given that there are several " + maximum[0] + "(s), the object could be a " + maximum[0] + " too\n"
				return
			
			else:
				# go through every object in Joe's room
				for j in rooms[i[1]-1][1]:
					if(j!=("person_" + i[0]) and j!="mistery_no_name"):
						joes_objects.add(j.split("_")[0])
			
				for j in room_types:
					for k in j:
						room_types_objects.add(k)
					
				# there's an object that doesn't fit in any room type, we can't use them
				if(len(joes_objects.difference(room_types_objects))>=1):
					for j,k in dictionary.items():
						if(k>maximum[1] and j!="mistery_no_name"):
							maximum = [j,k]
					print "\n> Given that there are several " + maximum[0] + "(s), the object could be a " + maximum[0] + " too\n"
					return
					
				# we can use the pre-established room types
				for j in room_types:
					aux = j.difference(joes_objects)
					
					# there's only one object missing, maybe the unidentified object is that one
					if(len(aux)==1 and len(j)==(len(joes_objects)+1)):
						for k in aux:
							print "\n> My guess is that the unidentified object close to Joe is a " + k + "\n"
							return
					
					# Joe's room matches perfectly a pre-established room type
					elif(j==joes_objects):
						room_type_temp = list(j)
						if(j==meeting_room):
							print "\n> My guess is that the unidentified object close to Joe is a chair\n"
							return
						
						string = "\n> The unidentified object is either a "
						
						for i in range(0,len(room_type_temp),1):
							if(i==(len(room_type_temp)-2)):
								string = string + room_type_temp[i] + " or a " + room_type_temp[i+1]
								break
							else:
								string = string + room_type_temp[i] + ", a "
						
						print string + "\n"
						
# ------------------------------------------------------------------------------------------------
# QUESTION 5 ("What is your estimate of the time it takes to visit all the rooms?") - DONE BY Nuno
def time_estimate():
	
	global times, time_room
	
	count = 1.0
	average = 0.0
	final = 0.0
	
	time_aux = (time.time() - time_room)
	
	if(times[current_global][0]==0):
		times[current_global][1] = time_aux
	
	for i in range(0,len(times),1): # calculate the average time spent in each room
		
		if(i==current_global):
			average += ((times[i][1]+time_aux)/2.0)
			count += 1.0
		
		elif(times[i][1]!=0.0):
			average += times[i][1]
			count += 1.0
		
	average = (average/count)
	
	for i in range(0,len(times),1): # get the final time
		
		if(i==current_global):
			final += ((times[i][1]+time_aux)/2.0)
		
		elif(times[i][1]!=0.0):
			final += times[i][1]
		
		else:
			final += average
		
	print "\n> You should expect to spend %.2fs\n" % (final)

# ------------------------------------------------------------------------------------------------------------------------
# QUESTION 6 ("How many different paths can you take to go from the current room, back to the start room?") - DONE BY João
def different_paths(current, start):
	
	global paths, graph, aux, current_global, visited
	aux2 = []
	
	for i in graph[current]:
		
		if(i==start): # we have reached our goal
			
			aux.append(start)
			paths.append(aux)
			aux2 = []
			print aux
			
			for j in aux: # reset aux so that it allows for further exploration
				if(j==current):
					aux2.append(j)
					break
				aux2.append(j)
			aux = aux2[:]
			
		else:
			if(i not in visited):
				visited.append(i)
				aux.append(i)
				different_paths(i,start)
				
				for j in aux: # reset aux so that it allows for further exploration
					if(j==current):
						aux2.append(j)
						break
					aux2.append(j)
				aux = aux2[:]
				
		if(current==current_global): # reset these variables (we are going to another neighbour of the starting node)
			visited = [current_global]
			aux = [current_global]
			
# --------------------------------------------------------------
# QUESTION 7 ("In what type of room is Mary in?") - DONE BY Nuno
def marys_room():
	
	global waiting_room, study_room, meeting_room, computer_lab, people
	
	mary = set()
	
	for i in people:
		if(i[0]=="mary"):
			# go through every object in Mary's room
			for j in rooms[i[1]-1][1]:
				if(j!=("person_" + i[0]) and j!="mistery_no_name"):
					mary.add(j)
					
	if(mary==waiting_room):
		print "\n> Mary is in a waiting room\n"
		
	elif(mary==study_room):
		print "\n> Mary is in a study room\n"
		
	elif(mary==computer_lab):
		print "\n> Mary is in a computer lab\n"
		
	elif(mary==meeting_room):
		print "\n> Mary is in a meeting room\n"
		
	else:
		print "\n> Mary is in a generic room\n"
	
# ------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 8 ("What is the probability of finding a chair in a room given that you already found a book in that room?") - DONE BY João
def chair_in_room():
	
	global dictionary, people
	
	books = 0
	total = 0
	chairs = 0
	
	for i,j in dictionary.items(): # get the amount of books and chairs in the observable world
		if(i=="book"):
			books = j
		elif(i=="chair"):
			chairs = j
		
		total += j
		
	total += len(people)
	
	if(total==0 or books==0):
		print "\n> I haven't seen any objects so far...\n"
		return
	
	print "\n> I reckon there's %.3f%% chance of that happening\n" % ((((float(chairs)/total)*(float(books)/total))/(float(books)/total))*100.0)

# -------------------------------------------------------------------------------------------------------
# QUESTION 9 ("What is the shortest path between the room you are in and the start room?") - DONE BY Nuno
def shortest_path(mode):
	
	global current_global, start_global, paths, aux, visited
	
	# prepare our global variables
	paths = []
	aux = [current_global]
	visited = [current_global]
	
	best_path = [0,0,0,0,0,0,0,0,0,0,0]
	string = ""
	
	different_paths(current_global, start_global)
	
	for i in paths:
		if(len(i)<=len(best_path)):
			best_path = i
	
	if(mode==1): # the "regular" shortest_path() function
		for j in range(0,len(best_path),1):
			if(j==(len(best_path)-1)):
				string = string + str(best_path[j]+1)
			else:
				string = string + str(best_path[j]+1) + " -> "
		
		print "\n> You should take this route: " + string + "\n"
	
	else: # the version of this function used for question 0 
		paths = best_path

# --------------------------------------------------------------------------
# QUESTION 0 ("Which is the best room to join Mary and Joe?") - DONE BY João
def join_people():
	
	global current_global, start_global, people
	
	for i in people: # get Mary and Joe's rooms
		if(i[0]=="mary"):
			current_global = (i[1]-1)
		elif(i[0]=="joe"):
			start_global = (i[1]-1)
	
	shortest_path(2)
	
	print "\n> The best room to join Mary and Joe is room " + str(paths[len(paths)/2]+1) + "\n"
	
# --------------------------------------------------------------------------------------------------------------------------------
# AUXILIARY FUNCTION - checks if the specified people have been seen by the robot (it avoids code repetition above) - DONE BY Nuno
def check_function(people_aux, function):
	
	global people
		
	if(len(people)==0):
		print "\n> I haven't seen any person yet\n"
		return
	
	for i in range(0,len(people),1):
		if(people[i][0]==people_aux[0]):
			break
		if(i==(len(people)-1)):
			print "\n> I haven't seen " + people_aux[0].capitalize() + " yet\n"
			return
	
	if(len(people_aux)==2):
		for i in range(0,len(people),1):
			if(people[i][0]==people_aux[1]):
				break
			if(i==(len(people)-1)):
				print "\n> I haven't seen " + people_aux[1].capitalize() + " yet\n"
				return
	function()

# -----------------
# odometry callback
def callback(data):
	
	global x_ant, y_ant, rooms, room_ant, current_global, graph, aux, movement, times, time_room
	
	x=data.pose.pose.position.x
	y=data.pose.pose.position.y
	
	# show coordinates only when they change
	if(round(x,1)!=x_ant or round(y,1)!=y_ant):
		x_ant = round(x,1)
		y_ant = round(y,1)
		room = robot_room()
		print "X=%.1f Y=%.1f (room %d)" % (x,y,room)
		
		if(movement==0): # the first time that the robot moves in the current room
			time_room = time.time()
			movement = 1
		
		if(rooms[room-1][0]==0):
			rooms[room-1][0]=1

		if(current_global+1)!=room: # the robot moved into another room
			time_aux = (time.time() - time_room)
			
			if((room-1) not in graph[room_ant-1]): # add edges to the graph if needed
				graph[room_ant-1].append(room-1)
				graph[room-1].append(room_ant-1)
			
			if(times[current_global][1]==0.0): # this is our first time value for this room
				times[current_global][1] = time_aux
				times[current_global][0] = 1
			
			else:
				times[current_global][1] = (times[current_global][1] + time_aux)/(2.0)
				times[current_global][0] += 1
			
			movement = 0
			
			print "\n> Time spent in the previous room (%d): %.2fs\n" % (current_global+1,time_aux)
			
			current_global = room-1
			aux[0] = current_global
			room_ant = current_global+1

# ---------------------------
# object_recognition callback
def callback1(data):
	
	global obj_ant, rooms, x_ant, y_ant, people, dictionary
	
	obj = data.data
	k = 1
	room = 0
	
	if(obj!=obj_ant and data.data!=""):
		print "\nObject is %s\n" % (data.data)
		
		aux = data.data.split(",") # get every object recognized just now
		room = robot_room()
		
		for i in aux:
			aux2 = i.split("_",1) # get this object's category
			
			if(aux2[0]!="person"):
				if(i not in rooms[room-1][1]): # update these room's inventory
					rooms[room-1][1].append(i)
					
					for i,j in dictionary.items(): # update the global dictionary of object categories
						
						if(i==aux2[0]): # this category already exists
							dictionary.update({aux2[0]:j+1})
							k=0
						
					if(k==1): # it's a brand new category
						dictionary.update({aux2[0]:1})
			
			else:
				if(i not in rooms[room-1][1]):
					people.append([aux2[1],room])
					rooms[room-1][1].append(i)
	obj_ant = obj
	
# ---------------------------
# questions_keyboard callback
def callback2(data):
	
	global paths, current_global, start_global, aux, visited
	
	print "\nQuestion is %s" % (data.data)
	
	if(data.data=="1"):
		objects_recognized()
	elif(data.data=="2"):
		objects_in_previous_room()
	elif(data.data=="3"):
		ten_books()
	elif(data.data=="4"):
		check_function(["joe"],object_joe)
	elif(data.data=="5"):
		if(movement==0):
			print "\n> My estimate only works if I start moving...\n"
		else:
			time_estimate()
	elif(data.data=="6"):
		if(current_global==start_global):
			print "\n> The start and current rooms are the same...\n"
			return
		
		# prepare these variables
		paths = []
		start_global = 0
		current_global = (robot_room()-1)
		aux = [current_global]
		visited = [current_global]
		
		different_paths(current_global,start_global)
		print graph
		
		final = ""
		string = ""
		print "\n> Here is every path between rooms " + str(current_global+1) + " and " + str(start_global+1) + ":"
		
		for i in paths:
			for j in range(0,len(i),1): # go through every path
				if(j==(len(i)-1)):
					string = string + str(i[j]+1)
				else:
					string = string + str(i[j]+1) + " -> "
			final = final + string + "\n"
			string = ""
			
		print final
		final = ""
	elif(data.data=="7"):
		check_function(["mary"],marys_room)
	elif(data.data=="8"):
		chair_in_room()
	elif(data.data=="9"):
		if(current_global==start_global):
			print "\n> The start and current rooms are the same...\n"
			return
		
		start_global = 0
		shortest_path(1)
	elif(data.data=="0"):
		check_function(["mary","joe"],join_people)

# ----------
def agent():
	
	rospy.init_node('agente')
	
	rospy.Subscriber("questions_keyboard", String, callback2)
	rospy.Subscriber("object_recognition", String, callback1)
	rospy.Subscriber("odom", Odometry, callback)
	print ""
	
	rospy.spin()

# ------------------------
if __name__ == '__main__':
	agent()
