import random
import hashlib
from Node import Node


def inputNodes(message):
	"""Check if the user's input is an integer"""
	while True:
		try:
			Userinput = int(raw_input(message))
		except ValueError:
			print("No valid integer! Please try again ...")
		else:
			return Userinput


def hashing(nodes, requests, keylist):
	"""Function that read the given file line by line and hash each string using SHA-1.

		"""
	hash_list = []
	with open('/Users/thanasiskaridis/Desktop/BigDataManagement/ChordImplementation/filenames.txt') as f:
		lines = random.sample(f.readlines(), requests)
		for line in lines:
			hash_object = hashlib.sha1(line)
			hash_key = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)
			hash_tuple = (hash_key, line.rstrip('\n'), random.choice(keylist))
			hash_list.append(hash_tuple)
	return hash_list


def create_nodes(nodes):

	diction = {}
	for i in range(nodes):
		node = Node(nodes)
		diction[node.hashed_ip] = node
	keylist = diction.keys()
	keylist.sort()
	return keylist, diction


def lookup(start, diction, nodes, count_messages):
	request = diction[start].message[1]
	next_message = (start, request)
	if request <= start:
		if diction[start].predecessor > diction[start].hashed_ip:
			if diction[start].predecessor <= request <= (2 ** nodes)-1 or 0 <= request <= diction[start].hashed_ip:
				return (start, count_messages)
			else:
				new_start = diction[start].finger_table[-1][1]
				diction[new_start].messages_list(next_message)
				count_messages += 1
				return lookup(new_start, diction, nodes, count_messages)
		else:
			if diction[start].predecessor <= request <= diction[start].hashed_ip:
				return (start, count_messages)
			else:
				new_start = diction[start].finger_table[-1][1]
				for k in diction[start].finger_table:
					if k[0] > k[1]:
						if k[0] <= request <= (2 ** nodes)-1 or 0 <= request <= k[1]:
							return k[1], count_messages
					else:
						if k[1] < request:
							new_start = k[1]
				diction[new_start].messages_list(next_message)
				count_messages += 1
				return lookup(new_start, diction, nodes, count_messages)
	else:
		max_num = [i for i in diction[start].finger_table if i[0] <= request]
		new_tuple = max(max_num, key = lambda item:item[0])
		if new_tuple[0] <= new_tuple[1]:
			if new_tuple[0] <= request <= new_tuple[1]:
				return (new_tuple[1], count_messages)
			else:
				diction[new_tuple[1]].messages_list(next_message)
				count_messages += 1
				return lookup(new_tuple[1], diction, nodes, count_messages)
		else:
			if new_tuple[0] <= request <= (2 ** nodes) - 1 or 0 <= request <= new_tuple[1]:
				return (new_tuple[1], count_messages)
			else:
				diction[new_tuple[1]].messages_list(next_message)
				count_messages += 1
				return lookup(new_tuple[1], diction, nodes, count_messages)