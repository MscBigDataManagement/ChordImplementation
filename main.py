import sys

class Node:
	"""A class that creates a Node"""
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

def main():
	#ask user to give the number of nodes
	# try:
	user_input = int(input("Enter the number of nodes n\n"))

	# the nodes that have been created will be added to a list which
	# shows all the alive nodes (In this project we suppose that every
	# node can not die)
	alive = []

	x = Node(1, 2)
	print x.ip, x.port

	# except ValueError:
	# 	print 'Error %s' % e
	# 	sys.exit(1)

if __name__ == "__main__":
	main()

