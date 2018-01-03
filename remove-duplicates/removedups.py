# -----------------------------------------------------------------------------------
#
#  	"Implement an algorithm to determine if a string has all unique characters.
#	 What if you cannot use an additional data structure*?"
#
#
#	This runs in O(n) time with O(n) space complexity. 
#
#	*Without using an additional data structure, it would take O(n^2) time to
#	 select each char and compare it against every other char in the string. 
#    Just like selection sort.
#
# ----------------------------------------------------------------------------------- 

def allUnique(str):
		 
	#	256 chosen to encapsulate all ASCII characters
	#  	A 'TRUE' under an index mean that character has
	# 	been seen already and we can exit allUnique(..)
	char_set = [False]*256;
	
	for i in range(0, len(str)):
		value = ord(str[i])
		
		if(char_set[value]):
			return False
		else:
			char_set[value] = True

	return True
	
 
def main():

	str = "uncle sam"
	
	if allUnique(str):
		print '\n', str, 'has all unique characters.\n'
	else:
		print '\n', str, 'does NOT have all unique characters.\n'

if __name__ == '__main__':
	main()


