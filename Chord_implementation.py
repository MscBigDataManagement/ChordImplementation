import func
from collections import Counter


def __main__():
	"""This function is the function main which calls all the other functions and runs the Chord Algorithm
	It also performs some measurements regarding the number of messages needed to locate a single file and the load of each node"""

	responsible_nodes = []
	messages_for_each = []
	list_nodes = []
	#flat_list = []

	# ask user to give the number of alive Nodes and the number of requests
	nodes = func.inputNodes("Enter the number of nodes \n ")

	# fill the ordered list of alive Nodes and a dictionary which has as key node and as value the movie
	keylist, diction = func.create_nodes(nodes)

	print "########Keylist"
	print keylist
	print "\n"
	
	# for each one of the nodes call the method predecessor_successor and the one that fills the finger_table
	for i in keylist:
		diction[i].predecessor_successor(keylist)
		diction[i].fill_finger_table(nodes,keylist)

	# fill a list of tuples
	hashed_req = func.hashing(nodes)

	for j in hashed_req:
		func.fill_requests(keylist, diction, j[0], j[2])

	# for k in diction.keys():
	# 	print diction[k].message

	func.read_requests(diction)









	# print "#######Request"
	# for i in hashed_req:
	# 	print i
	# 	print "\n"

	#print "\n"

	# for item in hashed_req:
	# 	first_message = (None, item[0])
	# 	diction[item[2]].messages_list(first_message)
	# 	counter_message = 1
	# 	list_nodes.append(item[2])
	# 	end = func.lookup(item[2], diction, nodes, counter_message, list_nodes)
	# 	responsible_nodes.append(end[0])
	# 	messages_for_each.append(end[1])
	#
	# print responsible_nodes
	#
	# print "\n"
	# print messages_for_each
	# print "\n"
	# print list_nodes
	# print "\n"
	#
	# occurencies_router = Counter(list_nodes)
	# print "Routing requests:", occurencies_router
	#
	# occurencies_requests = Counter(responsible_nodes)
	# print "File requests:", occurencies_requests
	#
	# """   EDW PREPEI NA KANOYME TIPOTA AVG H MEAN H KATI GIA NA VGALOUME SYMPERASMATA"""
	#
