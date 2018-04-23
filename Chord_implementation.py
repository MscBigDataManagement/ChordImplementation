import func


def __main__():
	"""This function will be called first. The implementation of Chord Algorithm"""
	responsible_nodes = []
	messages_for_each = []

	# ask user to give the number of alive Nodes and the number of requests
	nodes = func.inputNodes("Enter the number of nodes \n ")
	requests = func.inputNodes("Enter the number requests \n ")

	# fill the ordered list of alive Nodes and a dictionary which has as key node and as value the movie
	keylist, diction = func.create_nodes(nodes)

	print "########Keylist"
	print keylist
	print "\n"
	# print diction

	# for each one of the nodes call the method predecessor_successor and the one that fills the finger_table
	for i in keylist:
		diction[i].predecessor_successor(keylist)
		diction[i].fill_finger_table(nodes,keylist)

	# fill a list of tuples
	hashed_req = func.hashing(nodes, requests, keylist)

	print "#######Request"
	print hashed_req
	print "\n"

	for item in hashed_req:
		first_message = (None, item[0])
		diction[item[2]].messages_list(first_message)
		counter_message = 1
		end = func.lookup(item[2], diction, nodes, counter_message)
		responsible_nodes.append(end[0])
		messages_for_each.append(end[1])

	print responsible_nodes
	print messages_for_each
