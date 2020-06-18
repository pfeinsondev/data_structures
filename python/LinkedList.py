class Node:
	def __init__(self, val, next=False):
		self.val = val
		self.next = next

	def __str__(self):
		to_string = ("Value: " + str(self.val))
		return to_string
		
class LinkedList:
	def __init__(self, initial_value=False):
		if initial_value:
			self.root = Node(initial_value)
		else:
			self.root = Node(-99)
	
	def add(self, val):
		print("adding val " + str(val))
		if (self.root.next):
			scan = self.root.next
			while(scan.next): 
				scan = scan.next
			scan.next = Node(val)
		else:
			self.root.next = Node(val)

	def __str__(self):
		runner = self.root
		to_string = ""
		while (runner != False):
			to_string += str(runner) + "\t"
			runner = runner.next
		return to_string

test = LinkedList(10)
test.add(11)
test.add(12)
print(test)