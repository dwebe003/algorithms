#########################################################################################
#
#   File:       quicksort.py
#   Author:     David Weber (dwebe003)
#   Date:       Dec 19, 2017
#   Version:    1.0
#
#   Contents:   This is my Python representation of the classic QuickSort algorithm.
#				1) if numElements in array is 0 or 1, return
#				2) Pick any element p. this is our pivot.
#				3) Let S1 = {x in S\{p} | x <= p}  and  S2 = {x in S\{p} | x >= p}
#				4) Return quickSort(S1) followed by p followed by quickSort(S2)
#
#				Avg runtime: O(nlogn)		Worst case: O(n^2)
#
#########################################################################################

##------------ get pivot --------------##

def getPivot(a, left, right):
	
	# Obtains pivot using "median algorithm."
	# Picks 3 points and returns the median of them. 
	
	midpoint = (left + right)/2
	
	if(a[midpoint] < a[left]):
		temp = a[left]
		a[left] = a[midpoint]
		a[midpoint] = temp
		
	if(a[right] < a[left]):
		temp = a[left]
		a[left] = a[right]
		a[right] = temp
		
	if(a[right] < a[midpoint]):
		temp = a[midpoint]
		a[midpoint] = a[right]
		a[right] = temp
		
	temp = a[midpoint]
	a[midpoint] = a[right-1]
	a[right-1] = temp
	
	return a[right-1]

		
##---------- quick sort ------------------------------##

def quickSort(array, left, right):
	# Local variables
	i = left
	j = right
	pivot = getPivot(array, left, right)
	
	
	# Partitioning
	while( i <= j):
		while(array[i] < pivot):
			i += 1
		while(array[j] > pivot):
			j -= 1
		
		if(i <= j):
			# Swap
			temp = array[i]
			array[i] = array[j]
			array[j] = temp
			i += 1
			j -= 1
	#end while
	
	
	# Recursion
	if(left < j):
		quickSort(array, left, j)
	if(i < right):
		quickSort(array, i, right)

		
##------------- main ---------------------------------#

array = [5, 1, 9, 2, 4, 7, 0, 3, 8, 1, 2]

print 'before: ', array

quickSort(array, 0, len(array) - 1)

print 'after: ', array









