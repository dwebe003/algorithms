import collections

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.balanced = None
		self.height = 0
		

def isbalanced(tree):
	# create new tuple
	BalancedStatus = collections.namedtuple('BalancedStatus', ('balanced', 'height'))
	
	# recursive function
	def check_balanced(tree):
		if not tree:
			return BalancedStatus(True, -1)
		
		# check left subtree
		left_result = check_balanced(tree.left)
		if not left_result.balanced:
			return BalancedStatus(False, 0)
		
		# check right subtree
		right_result = check_balanced(tree.right)
		if not right_result.balanced:
			return BalancedStatus(False, 0)
			
		is_balanced = abs(left_result.height - right_result.height) <= 1
		height = max(left_result.height, right_result.height) + 1
		
		return BalancedStatus(is_balanced, height)
	
	return check_balanced(tree).balanced
				
	
 
def main():
	A = BinaryTreeNode(1)
	B = A.left = BinaryTreeNode(2)
	C = B.left = BinaryTreeNode(3)
	D = C.left = BinaryTreeNode(4)
	E = D.left = BinaryTreeNode(5)
	F = D.right = BinaryTreeNode(6)
	G = C.right = BinaryTreeNode(7)
	H = B.right = BinaryTreeNode(8)
	I = H.left = BinaryTreeNode(9)
	J = H.right = BinaryTreeNode(10)
	K = A.right = BinaryTreeNode(11)
	L = K.left = BinaryTreeNode(12)
	M = L.left = BinaryTreeNode(13)
	N = L.right = BinaryTreeNode(14)
	O = K.right = BinaryTreeNode(15)
	
	# the next line throws off the balance
	#X = E.right = BinaryTreeNode(16)
	
	if isbalanced(A):
		print 'balanced'
	else:
		print 'not balanced'
	

if __name__ == '__main__':
	main()


