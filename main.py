''' Big Data Management - Msc Data Science - 
    1st Programming Assignment
    
    Team Members:
    - Voulgari Eleni - A.M. 17005 - email: dsc17005@uop.gr
    - Karydis Athanasios - A.M. 17008 - email: dsc17008@uop.gr 
    
	Chord - based simulation of a distributed file system
'''

import hashlib
import random

class Node:
	"""A class that creates a Node"""

	def __init__(self,nodes):
		self.ip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":" + str(random.randint(0, 65535))
		hash_object = hashlib.sha1(self.ip)        
		self.hashed_ip = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)
		self.finger_table = []
		self.predecessor = 0
		self.successor = 0
		self.message = ()

	def predecessor_successor(self,keylist):
		for i in keylist:
			if i == self.hashed_ip:
				ind = keylist.index(i)
				self.predecessor = keylist[ind - 1]
				if ind != (len(keylist) - 1):
					self.successor = keylist[ind+1]
				else:
					self.successor = keylist[0]

	def fill_finger_table(self, nodes, keylist):
		next_node = 0
		for i in range(0, nodes):
			id = self.hashed_ip + 2 ** i
			if id >= (2 ** nodes):
				id2 = id - (2 ** nodes)
			else:
				id2 = id
			for j in keylist:
				if id > keylist[-1] and id < (2 ** nodes):
					next_node = keylist[0]
				elif j >= id2:
					next_node = j
					break
			record = (id, next_node)
			self.finger_table.append(record)

	def messages_list(self, message):
		self.message = message

def main():
	responsible_nodes = []
	messages_for_each = []
	#ask user to give the number of nodes
	nodes = int(input("Enter the number of nodes n\n"))
	requests = int(input("Enter the number requests \n"))
	keylist, diction = create_nodes(nodes)
	print "########Keylist"
	print keylist
	print "\n"
	# print diction
	for i in keylist:
		diction[i].predecessor_successor(keylist)
		diction[i].fill_finger_table(nodes,keylist)
        
	hashed_req = hashing(nodes, requests, keylist)
	print "#######Request"
	print hashed_req
	print "\n"
	for item in hashed_req:
		first_message = (None, item[0])
		diction[item[2]].messages_list(first_message)
		counter_message = 1
		end = lookup(item[2], diction, nodes, counter_message)
		responsible_nodes.append(end[0])
		messages_for_each.append(end[1])
	print responsible_nodes
	print messages_for_each

def hashing(nodes, requests, keylist):
	hash_list = []
	with open('filenames.txt') as f:
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
							return (k[1], count_messages)
					else:
						if k[1] < request:
							new_start = k[1]
				diction[new_start].messages_list(next_message)
				count_messages += 1
				return lookup(new_start, diction, nodes, count_messages)
	else:
		max_num = [i for i in diction[start].finger_table if i[0] <= request]
		new_tuple = max(max_num, key=lambda item:item[0])
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

if __name__ == "__main__":
	main()



