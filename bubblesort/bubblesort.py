#########################################################################################
#
#   File:       bubblesort.py
#   Author:     David Weber (dwebe003)
#   Date:       Dec 19, 2017
#   Version:    1.0
#
#   Contents:   This is just a quick Python implementation of the bubble sort algorithm.
#
#########################################################################################
		
##---------- bubble sort ------------------------------##

def bubbleSort(array):
	sz = len(array)
	
	for i in range(0, sz - 1):
		for j in range(sz-1, i, -1):
			if array[j] < array[j-1]:
				array[j], array[j-1] = array[j-1], array[j]
	
		
##------------- main ---------------------------------#

array = [5, 1, 9, 2, 4, 7, 0, 3, 8, 1, 2]

print 'before: ', array

bubbleSort(array)

print 'after: ', array









