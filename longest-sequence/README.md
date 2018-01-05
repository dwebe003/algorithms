## Intuition:
	For O(n) runtime, we add every number in the array to a new HashSet. This allows for easy
	lookup using the .contains(int val) function. We check every number, if it is the smallest
	number in some sequence, then we start checking how many times we can find a next number.
