#!/usr/bin/env python
# coding: utf8
import rospy
from std_msgs.msg import Int32,String
import sys
import tty

# ---------------------------------------------------------------
def questions():
	# node name
	rospy.init_node('questions_keyboard')
	pub=rospy.Publisher('questions_keyboard',String,queue_size=10)
	r = rospy.Rate(10)
	
	# show questions
	print '  1-How many different types of objects did you recognize until now?'
	print '  2-Which objects were in the room you visited before this one?'
	print '  3-What is the probability of finding 10 books in this world?'
	print '  4-What type of object do you think is the one without identification, that appears close to Paul?'
	print '  5-What is your estimate of the time it takes to visit all the rooms?'
	print '  6-How many different paths can you take to go from the current room, back to the start room?'
	print '  7-In what tipe of room is Mary in?'
	print '  8-What is the probability of finding a chair in a room given that you already found a book in that room?'
	print '  9-What is the shortest path between the room you are in and the start room?'
	print '  0-Which is the best room to join Mary and Joe?'
 
	tty.setcbreak(sys.stdin)

	while not rospy.is_shutdown():
		# read from keyboard
		k=sys.stdin.read(1)
		if int(k) < 0 or int(k) >9:
			continue
		pub.publish(k)
		#print 'Asked question: ' , k
		
# ---------------------------------------------------------------
if __name__ == '__main__':
	questions()
