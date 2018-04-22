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
		for i in range(nodes):
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

def main():
	#ask user to give the number of nodes
	nodes = int(input("Enter the number of nodes n\n"))
	requests = int(input("Enter the number requests \n"))

	hashed_req = hashing(nodes, requests)


	keylist, dict = create_nodes(nodes)
	print keylist

	for i in keylist:
		dict[i].predecessor_successor(keylist)
		dict[i].fill_finger_table(nodes,keylist)
		print dict[i].finger_table



def hashing(nodes, requests):
	hash_list = []
	with open('filenames.txt') as f:
		lines = random.sample(f.readlines(), requests)
		for line in lines:
			hash_object = hashlib.sha1(line)
			hash_key = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)
			hash_list.append(hash_key)
	return hash_list

def create_nodes(nodes):
	dict = {}
	for i in range(nodes):
		node = Node(nodes)
		dict[node.hashed_ip] = node
	keylist = dict.keys()
	keylist.sort()
	return keylist, dict


if __name__ == "__main__":
	main()



