#########################################################################################
#
#   File:       bucketsort.py
#   Author:     David Weber (dwebe003)
#   Date:       Dec 19, 2017
#   Version:    1.0
#
#   Contents:   This is just a quick Python implementation of the bucket sort algorithm.
#
#########################################################################################
		
##---------- bucket sort ------------------------------##

def bucketSort(array):
	
	buckets = []
	
	for i in range(0, 101):
		buckets.append(0)
	
	for i in range(0, len(array)):
		buckets[array[i]] += 1
		
	i = 0
	for j in range(0, 101):
		for k in range(buckets[j], 0, -1):
			array[i] = j
			i += 1
		
	
		
##------------- main ---------------------------------#

array = [5, 1, 9, 2, 4, 7, 0, 3, 8, 1, 2]

print 'before: ', array

bucketSort(array)

print 'after: ', array









