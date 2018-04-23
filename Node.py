import hashlib
import random


class Node:
	"""This class creates a Node obstacle. It includes the above methods:
	A constructor which creates the object of Node, when the class is called.
	A method which can find the predecessor and the successor of the node
	A method which fill the Finger Table which is used in order to perform the
	Chord algorithm
	##############################A method which"""

	def __init__(self,nodes):
		# creates an ip including port in order to have the form xxx.xxx.xxx.xxx:xxxx
		self.ip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":" + str(random.randint(0, 65535))
		hash_object = hashlib.sha1(self.ip)        #
		self.hashed_ip = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)
		self.finger_table = []
		self.predecessor = 0
		self.successor = 0
		self.message = ()

	def predecessor_successor(self, keylist):
		"""Method that get the sorted list of all alive nodes and gives as a result the predecessor
		and the successor of the node"""

		for i in keylist:
			if i == self.hashed_ip:
				ind = keylist.index(i)
				self.predecessor = keylist[ind - 1]
				if ind != (len(keylist) - 1):
					self.successor = keylist[ind+1]
				else:
					self.successor = keylist[0]

	def fill_finger_table(self, nodes, keylist):
		"""Method that get the sorted list of all alive nodes,
		the number of nodes and fill the Finger Table of the node"""

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
		"""???????????????????????????????????????"""
		self.message = message