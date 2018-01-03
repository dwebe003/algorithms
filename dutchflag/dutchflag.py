#########################################################################################
#
#   File:       dutchflag.py
#   Author:     David Weber (dwebe003)
#   Date:       Dec 19, 2017
#   Version:    1.0
#
#   Contents:   This is just a quick Python implementation of dutch flag.
#
#########################################################################################
		
##---------- dutch flag ------------------------------##

def dutchFlag(array):
	
	low = 0
	mid = 0
	high = len(array) - 1
	
	while mid <= high:
		if array[mid] == 2:
			array[mid], array[high] = array[high], array[mid]
			high -= 1
		elif array[mid] == 0:
			array[low], array[mid] = array[mid], array[low]
			mid += 1
			low += 1
		else:
			mid += 1
	
		
##------------- main ---------------------------------#

array = [2, 1, 0, 1, 0, 2, 1, 1, 0, 2, 2]

print 'before: ', array

dutchFlag(array)

print 'after: ', array









