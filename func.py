import random
import hashlib
from Node import Node
import math
from scipy.stats import powerlaw


def inputNodes(message):
	"""Check if the user's input is an integer"""

	while True:
		try:
			Userinput = int(raw_input(message))
		except ValueError:
			print("No valid integer! Please try again ...")
		else:
			return Userinput


def hashing(nodes):
	"""Function that read the given file line by line and hash each string using SHA-1.
	The function returns a list of tuples. Each tuple has the requested item, the file's name and a random start"""

	hash_list = []
	ring = int(math.log(nodes,2)) + 1
	with open('test.txt') as f:
		count = 0
		lines = f.readlines()
		print len(lines)
		popularity = powerlaw.rvs(1.65, size=len(lines), discrete=True, scale=10)
		print popularity
		for line in lines:
			hash_object = hashlib.sha1(line)
			hash_key = int(hash_object.hexdigest(), 16) % (2 ** ring)
			hash_tuple = (hash_key, line.rstrip('\n'), popularity[count])
			hash_list.append(hash_tuple)
			count += 1
	return hash_list


def create_nodes(nodes):
	""" This function gets the # of nodes as input. It creates a dictionary with node's hashed ip as key and as value the node object
	From this dictionary we export a list which contains the keys of the dictionary sorted from min to max"""

	diction = {}
	for i in range(nodes):
		node = Node(nodes)
		diction[node.hashed_ip] = node
	keylist = diction.keys()
	keylist.sort()
	return keylist, diction


def fill_requests(keylist, diction, movie, popularity):
	for i in range(popularity):
		diction[random.choice(keylist)].messages_list(movie)


def read_requests(diction):
	for start in diction.keys():
		lookup(diction, start, diction[i].message[0])


def lookup(diction, start, request):
	pass

# def lookup(start, diction, nodes, count_messages, list_nodes):
# 	"""This function is the implementation of the lookup in the Chord. With this lookup the algorithm searches for the Node that has
# 	the requested item"""
#
# 	request = diction[start].message[1]
# 	next_message = (start, request)
#
# 	ring = int(math.log(nodes,2)) + 1
#
# 	if request <= start:
# 		if diction[start].predecessor > diction[start].hashed_ip:
# 			if diction[start].predecessor <= request <= (2 ** ring)-1 or 0 <= request <= diction[start].hashed_ip:
# 				count_messages = count_messages - 1
# 				return (start, count_messages, list_nodes)
# 			else:
# 				new_start = diction[start].finger_table[-1][1]
# 				diction[new_start].messages_list(next_message)
# 				count_messages = count_messages + 1
# 				list_nodes.append(new_start)
# 				return lookup(new_start, diction, nodes, count_messages, list_nodes)
# 		else:
# 			if diction[start].predecessor <= request <= diction[start].hashed_ip:
# 				count_messages = count_messages - 1
# 				return (start, count_messages, list_nodes)
# 			else:
# 				new_start = diction[start].finger_table[-1][1]
# 				for k in diction[start].finger_table:
# 					if k[0] > k[1]:
# 						if k[0] <= request <= (2 ** ring)-1 or 0 <= request <= k[1]:
# 							return (k[1], count_messages, list_nodes)
# 					else:
# 						if k[1] < request:
# 							new_start = k[1]
# 				diction[new_start].messages_list(next_message)
# 				count_messages = count_messages + 1
# 				list_nodes.append(new_start)
# 				return lookup(new_start, diction, nodes, count_messages, list_nodes)
# 	else:
# 		max_num = [i for i in diction[start].finger_table if i[0] <= request]
# 		new_tuple = max(max_num, key = lambda item:item[0])
# 		if new_tuple[0] <= new_tuple[1]:
# 			if new_tuple[0] <= request <= new_tuple[1]:
# 				return (new_tuple[1], count_messages, list_nodes)
# 			else:
# 				diction[new_tuple[1]].messages_list(next_message)
# 				count_messages += 1
# 				list_nodes.append(new_tuple[1])
# 				return lookup(new_tuple[1], diction, nodes, count_messages, list_nodes)
# 		else:
# 			if new_tuple[0] <= request <= (2 ** ring) - 1 or 0 <= request <= new_tuple[1]:
# 				return (new_tuple[1], count_messages, list_nodes)
# 			else:
# 				diction[new_tuple[1]].messages_list(next_message)
# 				count_messages = count_messages + 1
# 				list_nodes.append(new_tuple[1])
# 				return lookup(new_tuple[1], diction, nodes, count_messages, list_nodes)