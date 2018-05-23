
"""
Liear search algorithm recursive form
returns the index of the search element. this implements list 
Args:
		x (int): The element to be searched
		lst (int): The first parameter. its supposed to be a sorted array
Returns:
		returns the index where the element is found (1st hit only) 
		returns -1 if not found
"""

"""defining recursive linear search algorithm 
	lookat the 1st element, if that is not THE element, look for the element in remaining subarray. pass down the index for bookkeeping
	if the element is found return the 


"""
def linsearch(x,lst, idx = 0):
	##recursive call to linearly search the array. array may not be sorted
	#base case start with 0
	if len(lst) == 0 or idx >= len(lst):
		return -1
	
	
	if x != lst[idx]:
		return linsearch(x,lst,idx+1)
	elif x == lst[idx]:
		return idx
	else:
		return -1


t = int(input())

for i in range(0,t):
		n = int(input())
		lst = list(map(int, input().split()))
		#print(lst)
		print( str(linsearch(int(input()),lst)))
	