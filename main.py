import hashlib
import random



class Node:
	"""A class that creates a Node"""
	predecessor = 0
	successor = 0
	finger_table =[]

	def __init__(self,nodes):
		self.ip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":" + str(random.randint(0, 65535))
		# self.hashed_ip = hash(nodes)
		hash_object = hashlib.sha1(self.ip)
		self.hashed_ip = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)

	def predecessor_successor(self,keylist):
		for i in keylist:
			if i == self.hashed_ip:
				ind = keylist.index(i)
				self.predecessor = keylist[ind - 1]
				if ind != (len(keylist) - 1):
					self.successor = keylist[ind+1]
				else:
					self.successor = keylist[0]

	def finger_table(self):
		pass

def main():
	#ask user to give the number of nodes
	nodes = int(input("Enter the number of nodes n\n"))
	requests = int(input("Enter the number requests \n"))

	hashed_req = hashing(nodes, requests)
	# print hashed_req


	keylist, dict = create_nodes(nodes)
	print keylist
	for i in keylist:
		dict[i].predecessor_successor(keylist)
		print dict[i].successor
		print dict[i].predecessor
		print "\n"






def hashing(nodes, requests):
	hash_list = []
	with open('/Users/thanasiskaridis/Desktop/BigDataManagement/ChordImplementation/filenames.txt') as f:
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



