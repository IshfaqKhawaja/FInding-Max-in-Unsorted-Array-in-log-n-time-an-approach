#Finding max in log time:
import random
array = []
for i in range(10000):
	array.append(random.randint(0,20000))
print('Maximum of array using Python Function ' ,max(array))
print('Size of array is ', len(array))
maximum = array[0]
count = 0

def find_max(array):
	global maximum
	global count
	if len(array)>1:
		mid = len(array)//2
		L = array[:mid]
		R = array[mid:]
		find_max(L)
		find_max(R)
		count+=1
		if len(array)<=3:#Work here and try to reduce complexity
			for i in array:
				if i > maximum:
					maximum = i

find_max(array)
print('Maximum in array is ', maximum)
print('Count is ', count)




















##
### Python program for implementation of MergeSort
##count = 0
##def mergeSort(arr):
##	global count
##	if len(arr) > 1:
##				# Finding the mid of the array
##		mid = len(arr)//2
##
##		# Dividing the array elements
##		L = arr[:mid]
##
##		# into 2 halves
##		R = arr[mid:]
##
##		# Sorting the first half
##		mergeSort(L)
##
##		# Sorting the second half
##		mergeSort(R)
##		count+=1
##		print(count)
##
##		i = j = k = 0
##
##		# Copy data to temp arrays L[] and R[]
##		while i < len(L) and j < len(R):
##			if L[i] < R[j]:
##				arr[k] = L[i]
##				i += 1
##			else:
##				arr[k] = R[j]
##				j += 1
##			k += 1
##
##		# Checking if any element was left
##		while i < len(L):
##			arr[k] = L[i]
##			i += 1
##			k += 1
##
##		while j < len(R):
##			arr[k] = R[j]
##			j += 1
##			k += 1
##
### Code to print the list
##
##
##def printList(arr):
##	for i in range(len(arr)):
##		print(arr[i], end=" ")
##	print()
##
##
### Driver Code
##if __name__ == '__main__':
##	arr = [9,4,3,2,10,12,14,-2,6,0,20, 10, 20, 4, 100]
##	print("Given array is", end="\n")
##	printList(arr)
##	mergeSort(arr)
##	print("Sorted array is: ", end="\n")
##	printList(arr)
##
### This code is contributed by Mayank Khanna
