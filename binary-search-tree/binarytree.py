

##------------ node struct --------------##
class Node:
	
	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None
		self.depth = None
	#end
	

	def printKids(self):
		if self is not None:
			#print self.value
			
			if self.left is not None:
				print(self.left.value, '- depth', self.left.depth, ', parent:', self.value)
			if self.right is not None:
				print(self.right.value, '- depth', self.right.depth, ', parent:', self.value)
			
			if self.left is not None:
				self.left.printKids()
			if self.right is not None:
				self.right.printKids()
	#end
				
				
	def insert(self, value):

		if self is None:
			self = Node(value)
			
		if(value < self.value):
			if self.left is None:
				self.left = Node(value)
				self.left.depth = self.depth + 1
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = Node(value)
				self.right.depth = self.depth + 1
			else:
				self.right.insert(value)
		
		return self
	#end
		
		
def find(root, x):
	
	if root is None:
		return None
	
	if(root.value == x):
		print('item',x,'found')
	
	if(x < root.value):
		find(root.left, x)
	else:
		find(root.right, x)
	
	
##---------- binary tree ------------------------------##
class BinaryTree:

	
	def __init__(self, val):
		self.root = Node(val)
		self.root.depth = 1
	#end
		
		
	def insert(self, value):

		if self.root is None:
			self.root = Node(value)
			
		if(value < self.root.value):
			if self.root.left is None:
				self.root.left = Node(value)
				self.root.left.depth = self.root.depth + 1
			else:
				self.root.left.insert(value)
		else:
			if self.root.right is None:
				self.root.right = Node(value)
				self.root.right.depth = self.root.depth + 1
			else:
				self.root.right.insert(value)
		
		return self.root
	#end
	

	
		
	def printTree(self):
		print(self.root.value, '- depth 1 , parent: null')
		self.root.printKids()
	#end
		
		
##------------- main ---------------------------------#
# Initializes tree
tree = BinaryTree(50)

# Tests insert function
tree.insert(30)
tree.insert(70)
tree.insert(40)
tree.insert(80)
tree.insert(45)

# Tests search function
x = find(tree.root, 90)
if x is None:
	print('item 90 not found')
x = find(tree.root, 80)

# Prints tree
tree.printTree()









