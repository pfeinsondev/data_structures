#--------#
#  Node  #
#--------#
class Node:
	def __init__(self, val):				# Constructor - Accepts value
		self.val = val						# Set node value
		self.left_child = False					# Set left_child to False
		self.right_child = False				# Set right_child to False	
	
	def has_left_child(self):				# has_left_child
		if (self.left_child != False):
			return True
		else:
			return False

	def has_right_child(self):				# has_right_child 
		if (self.right_child != False):
			return True
		else:
			return False


	def __str__(self):					# to string
		return str(self.val)				# return the value of this Node
#-------#
#  BST  #
#-------#	
class BST:
	def __init__(self, val):				# Constructor - Accepts value
		self.root = Node(val)					# root = new Node with given value	

	def add(self, val, focus=False):			# Accepts value, if focus not given, set it to False
		if not (focus):					# If focus wasn't given
			focus = self.root				# Set it to root
		if (val < focus.val):				# If new value is less than focus.val
			if (focus.left_child):				# If it has left children
				self.add(val, focus.left_child)			# Recurse left
			else:						# If it doesn't
				focus.left_child = Node(val)			# Add it
		else:						# If the new value is greater than or equal to focus.val
			if (focus.right_child):				# If it has a right child
				self.add(val, focus.right_child)		# Recurse right
			else:						# If it doesn't
				focus.right_child = Node(val)			# Add it

	def print_ascending(self, focus=False):
		if not (focus):					# Base Case (First Pass)
			focus = self.root				# Set focus to root
		if (focus.left_child):				# If it has left children
			self.print_ascending(focus.left_child) 		# Recurse left		
		print(focus.val)
		if (focus.right_child):				# If it has right children
			self.print_ascending(focus.right_child)		# Recurse right
	
	def print_descending(self, focus=False):
		if not (focus):
			focus = self.root
		if (focus.has_right_child()):
			self.print_descending(focus.right_child)
		print(focus.val)
		if (focus.has_left_child()):
			self.print_descending(focus.left_child)

	def find(self, val, focus=False):					# Finds value in BST / Search
		if not focus:							
			focus = self.root						
		if (focus.val == val):					
			return True
		elif (focus.has_left_child() and (focus.val > val)):
			return self.find(val, focus.left_child)				
		elif (focus.has_right_child() and (focus.val < val)):	
			return self.find(val, focus.right_child)				
		return  False							
			

#----------#
#   Test   #
#----------#
test = BST(14)
test.add(16)
test.add(15)
test.add(11)
test.add(13)
test.add(9)
test.add(12)
test.print_ascending()