#--------#
#  Node  #
#--------#
class Node:
	def __init__(self, val):	# Constructor (accepts val)
		self.val = val			# Set node value to val
		self.next = False		# Set next and prev to False
		self.prev = False

	def __str__(self):					# To string
		to_string = ("Value: " + str(self.val))			# Make value readable
		return to_string
#-------#					
#  DLL  #
#-------#		
class DoublyLinkedList:
	def __init__(self, initial_value):			# Constructor,  accepts initial value
		if initial_value:					# If there was an initial value
			self.root = Node(initial_value)			# Set root to a node containing that value
			self.tail = self.root				# Set tail to root


	def add(self, val):
		print("adding val " + str(val))
		if (self.root != self.tail):	 		# If there are already 2+ nodes
			self.tail.next = Node(val)			# add new node to end
			self.tail.next.prev = self.tail			# set the new nodes prev to tail
			self.tail = self.tail.next			# reassign tail to tail.next 
		else:						# If this is the second node
			self.tail = Node(val)				# tail = new Node
			self.tail.prev = self.root			# set 'tail' prev to root
			self.root.next = self.tail			# set root.next to tail
			

	def __str__(self):					# to_string
		runner = self.root					# create 'pointer' node; point to root
		to_string = ""						
		while (runner != False):				# while the pointer isn't pointing to nothing
			to_string += str(runner) + "\t"				# Append current Nodes value to the returned string + a tab
			runner = runner.next					# move runner to point to next node
		return to_string					# Return string

#--------#
#  Test  #
#--------#
test = DoublyLinkedList(10)
test.add(11)
test.add(12)
test.add(13)
test.add(14)
print(test)