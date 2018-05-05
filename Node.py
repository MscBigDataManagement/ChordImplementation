import hashlib
import random
import math


class Node:
	"""This class creates a Node obstacle. It includes the above methods:
	- A constructor which creates the object of Node, when the class is called.
	- A method which finds the predecessor and the successor of the node.
	- A method which fills the Finger Table used to perform the Chord algorithm.
	- A method which gets a message and stores it in each node."""

	def __init__(self,nodes):
		"""The constructor creates the instant of a Node.
		It also initialises its variables.
		At the same time it gives a value to the ip of the node.
		More specifically, it creates an ip including a port in order to have the form xxx.xxx.xxx.xxx:xxxx.
		Then the ip is hashed by using SHA-1 """
		# ring = int(math.log(nodes,2)) + 1
		self.ip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":" + str(random.randint(0, 65535))
		hash_object = hashlib.sha1(self.ip)
		self.hashed_ip = int(hash_object.hexdigest(), 16) % (2 ** 160)
		self.finger_table = []
		self.predecessor = 0
		self.successor = 0
		self.message = []
		self.msg = ()

	def predecessor_successor(self, keylist):
		"""Method that gets the sorted list of all alive nodes and gives as a result the predecessor
		and the successor of the node"""

		for i in keylist:
			if i == self.hashed_ip:
				ind = keylist.index(i)                  # finds the index of the node's ip into the list
				self.predecessor = keylist[ind - 1]     # gives the value of the previous indexed item to predecessor (in case of first item
														# the predecessor is the last item of the list)
				if ind != (len(keylist) - 1):           # the value of the next item in the list is the successor
					self.successor = keylist[ind+1]
				else:
					self.successor = keylist[0]         # case of last item. The successor is the first element of the list

	def fill_finger_table(self, nodes, keylist):
		"""Method that gets the sorted list of all alive nodes,
		the number of nodes and fills the Finger Table of the node"""

		next_node = 0
		ring = int(math.log(nodes,2)) + 1
		for i in range(0, nodes):
			id = self.hashed_ip + 2 ** i
			if id >= (2 ** 160):
				id2 = id - (2 ** 160)
			else:
				id2 = id
			for j in keylist:
				if id > keylist[-1] and id < (2 ** 160):
					next_node = keylist[0]
				elif j >= id2:
					next_node = j
					break
			record = (id, next_node)
			self.finger_table.append(record)
		# print self.finger_table
		# print "\n"

	def messages_list(self, message):
		"""Method that gets a message for a node and writes it in its message space"""
		self.message.append(message)

	def msg_to_next(self, msg):
		self.msg = msg
