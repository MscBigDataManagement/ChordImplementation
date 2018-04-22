import hashlib
import random

class Node:
	"""A class that creates a Node"""
	predecessor = 0
	successor = 0

	def __init__(self,nodes):
		self.ip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":" + str(random.randint(0, 65535))
		hash_object = hashlib.sha1(self.ip)        
		self.hashed_ip = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)
		self.finger_table = []
		self.responsible = ()

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

	def responsibility(self):
		self.responsible = (self.predecessor+1, self.hashed_ip)
		return self.responsible

def main():
	#ask user to give the number of nodes
	nodes = int(input("Enter the number of nodes n\n"))
	requests = int(input("Enter the number requests \n"))
	keylist, dict = create_nodes(nodes)
	print keylist
	# print dict
	for i in keylist:
		dict[i].predecessor_successor(keylist)
		dict[i].responsibility()
		print dict[i].responsible
		dict[i].fill_finger_table(nodes,keylist)
	hashed_req = hashing(nodes, requests, keylist)
	# print hashed_req
	for item in hashed_req:
		end = lookup(item[0], item[2], dict)


def hashing(nodes, requests, keylist):
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
	dict = {}
	for i in range(nodes):
		node = Node(nodes)
		dict[node.hashed_ip] = node
	keylist = dict.keys()
	keylist.sort()
	return keylist, dict

def lookup(request, start,dict):
	# print dict[start].finger_table
	if request <= start:
		if dict[start].responsible[0] <= request <= dict[start].responsible[1]:
			return start
		else:
			for k in dict[start].finger_table:
				if k[1] <= request:
					new_start = k[1]
					return lookup(request, new_start, dict)
			new_start = dict[start].finger_table[-1][1]
			return lookup(request, new_start, dict)
	elif request > dict[start].finger_table[-1][0]:
		new_start = dict[start].finger_table[-1][1]
		return lookup(request, new_start, dict)
	else:
		for i in dict[start].finger_table:
			if request == i[0]:
				if i[1].responsible[0] <= request <= i[1].responsible[1]:
					return i[1]
			elif request > i[0]:
				ind = i.index(i[0])
				new_start = dict[start].finger_table[ind - 1][1]
				return lookup(request, new_start, dict)

if __name__ == "__main__":
	main()



