
"""
Binary search algorithm
returns the index of the search element. this implements list 
Args:
		x (int): The element to be searched
		lst (int): The first parameter. its supposed to be a sorted array
		lo (int): lower index of the subarray to be searched
		hi (int): higher index of the subarray to be searched
Returns:
		returns the index where the element is found (1st hit only) 
		returns -1 if not found
"""
def binsearch(x,lst,lo,hi):
	##recursive call to search the sorted array. Assuming array is sorted.
	mid = int((lo + hi)/2)
	if x < lst[mid]:
		return binsearch(x,lst,lo,mid)
	elif x > lst[mid]:
		return binsearch(x,lst,mid,hi)
	elif x == lst[mid]:
		return mid
	else:
		return -1


t = int(input())

for i in range(0,t):
		n = int(input())
		lst = list(map(int, input().split()))
		lst.sort()
		#print(lst)
		print( str(binsearch(int(input()),lst,0,n-1)) )
