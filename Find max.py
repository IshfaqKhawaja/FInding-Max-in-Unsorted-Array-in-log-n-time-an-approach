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
