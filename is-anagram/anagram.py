

def isAnagram(str1, str2):
	
	# initial check of length. It is obvious that two strings of
	# unequal length cannot be anagrams.
	if len(str1) != len(str2):
		return false;
		 
	# initialize an array of char values for each string.
	# we will iterate through each string and increment
	# whatever value is seen
	hits1 = [0]*256;
	hits2 = [0]*256;
	
	# actual iterations
	for i in range(0, len(str1)):
		hits1[ord(str1[i])] += 1
		hits2[ord(str2[i])] += 1
	
	# looking for a char value that does not equal its corresponding
	# value in the other string. if none found then AWESOME-- they're anagrams.
	for j in range(0, 256):
		if hits1[j] != hits2[j]:
			return False
	
	return True
	
 
def main():

	str1 = "uncle sam"
	
	str2 = "samen luc"
	
	str3 = "uncle bob"
	
	if isAnagram(str1, str2):
		print str1, 'and', str2, 'are anagrams.'
	else:
		print str1, 'and', str2, 'are NOT anagrams.'
	
	if isAnagram(str1, str3):
		print str1, 'and', str3, 'are anagrams.'
	else:
		print str1, 'and', str3, 'are NOT anagrams.'

if __name__ == '__main__':
	main()


