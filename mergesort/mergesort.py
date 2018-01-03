#########################################################################################
#
#   File:       mergesort.py
#   Author:     David Weber (dwebe003)
#   Date:       Dec 19, 2017
#   Version:    1.0
#
#   Contents:   This is my Python representation of the MergeSort algorithm. It 
#				recursively dissects the array into left and right segments until
#				single elements are reached, at which point merge(..) is called to
#				assemble them back together in a sorted fashion. 
#
#
#	A quick visual (tree) representation of what is happening...
#
#							5 1 9 2 4 7 0 3 8 1 2
#					 5 1 9 2 4 7			     0 3 8 1 2
#				5 1 9		  2 4 7	 		0 3 8		  1 2
#			 5 1	  9    2 4   	7 	  0 3     8		1	   2
#		    5    1	  	  2   4			 0    3
#
#	Merge(..) is now called... 
#							5 1 9 2 4 7 0 3 8 1 2
#					 5 1 9 2 4 7			     0 3 8 1 2
#				5 1 9		  2 4 7	 		0 3 8		  1 2
#			 1 5	  9    2 4   	7 	  0 3     8		1	   2
#
#	Notice the 1 and 5 are now sorted. 2 4   and   0 3 already in sorted order. 
#
#########################################################################################

##------------ merge --------------##
def merge(array, left, mid, right):
	i = left
	j = mid + 1
	k = 0
	tempArr = []
	
	# Merges each sub-array back together in sorted order (recursively in mergeSort)
	while(i <= mid and j <= right):
		if(array[i] <= array[j]):
			entry = array[i]
			tempArr.append(entry)
			i += 1
		else:
			entry = array[j]
			tempArr.append(entry)
			j += 1
	
	# Adds remainder of left-side to tempArr
	while(i <= mid):
		entry = array[i]
		tempArr.append(entry)
		i += 1
		
	# Adds remainder of right-side to tempArr
	while(j <= right):
		entry = array[j]
		tempArr.append(entry)
		j += 1
	
	# Copy contents back to original array
	for i in range(left, right + 1):
		array[i] = tempArr[i - left]
		
##---------- merge sort ------------------------------##
def mergeSort(array, left, right):
	
	
	if(left < right):
		midpoint = (left + right) / 2
		mergeSort(array, left, midpoint)
		mergeSort(array, midpoint + 1, right)
		merge(array, left, midpoint, right)
		
		
##------------- main ---------------------------------#

array = [5, 1, 9, 2, 4, 7, 0, 3, 8, 1, 2]

print 'before: ', array

mergeSort(array, 0, len(array) - 1)

print 'after: ', array









