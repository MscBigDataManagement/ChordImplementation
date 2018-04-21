import hashlib
import random



class Node:
	"""A class that creates a Node"""
	predecessor = 0
	successor = 0
	finger_table =[]

	def __init__(self,nodes):
		self.ip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":" + str(random.randint(0, 65535))
		self.hashed_ip = hash(nodes)

	def __predeccessor__(self):
		Node.finger_table = 1

	def successor(self):
		pass

	def finger_table(self):
		pass

	def hash(self,nodes):
		hash_object = hashlib.sha1(self.ip)
		return int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)

def main():
	#ask user to give the number of nodes
	nodes = int(input("Enter the number of nodes n\n"))
	requests = int(input("Enter the number requests \n"))

	hashed_req = hashing(nodes, requests)
	# print hashed_req

	x = Node(nodes)
	print x.ip
	print x.hashed_ip

def create_node():


def hashing(nodes, requests):
	hash_list = []
	with open('/Users/thanasiskaridis/Desktop/BigDataManagement/ChordImplementation/filenames.txt') as f:
		lines = random.sample(f.readlines(), requests)
		for line in lines:
			hash_object = hashlib.sha1(line)
			hash_key = int(hash_object.hexdigest(), 16) % ((2 ** nodes) - 1)
			hash_list.append(hash_key)
	return hash_list


if __name__ == "__main__":
	main()



