import func
from collections import Counter

def __main__():
	"""This function is the function main which calls all the other functions and runs the Chord Algorithm
	It also performs some measurements regarding the number of messages needed to locate a single file and the load of each node"""

	# ask user to give the number of requests
	requests = func.checkInputs("Enter the number of Requests \n ")
	# ask user to give the number of alive Nodes
	nodes = func.checkInputs("Enter the number of nodes \n ")

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
	hashed_req = func.hashing(requests, nodes)

	for j in hashed_req:
		func.fill_requests(keylist, diction, j[0], j[2])

	all_requests = []
	for k in diction.keys():
		print diction[k].message
		all_requests.append(diction[k].message)
	print "all-requests"
	all_requests = [item for sublist in all_requests for item in sublist]

	print all_requests
	responsible_nodes, messages_for_each, list_nodes = func.read_requests(diction, nodes)


	tot_messages = {}
	my_tuples = zip(all_requests, messages_for_each)
	for x, y in my_tuples:
		tot_messages.setdefault(x, []).append(y)
	print tot_messages

	for item in tot_messages.keys():
		tot_messages[item] = sum(tot_messages[item])/float(len(tot_messages[item]))
	print tot_messages

	print "#######Request"
	for i in hashed_req:
		print i
		print "\n"

	print "\n"


	print "responsible nodes"
	print len(responsible_nodes)
	print responsible_nodes
	print "\n"
	print "messages_for_each"
	print messages_for_each
	print "\n"
	print "list_nodes"
	print list_nodes
	print "\n"

	occurencies_router = Counter(list_nodes)
	print "Routing requests:", occurencies_router

	occurencies_requests = Counter(responsible_nodes)
	print "File requests:", occurencies_requests


