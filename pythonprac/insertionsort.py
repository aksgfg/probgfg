# insertion sort algorithm
"""
Insertion sort algorithm
returns the sorted array 
Args:
		x (int): The element to be searched
		lst (int): The first parameter. its supposed to be a sorted array
Returns:
		returns the index where the element is found (1st hit only) 
		returns -1 if not found
"""
def insertionsort(arr):
	for j in range(2,len(arr)):
		i=j-1
		key = arr[j]
		while i>0 and arr[i] > key:
			arr[i+1] = arr[i]
			i = i - 1
		arr[i+1] = key

arr = [1,2,4,3,10,6,9,7,3,5,8]
insertionsort(arr);
print(arr)