#merge sort algorithm
"""
Merge sort algorithm is based on divide and conquer technique of solving problems.
this program will have 2 parts one main algorithm which is recursive and unfolds the
recursion tree (mergesort(arr)) and another (merge(arr,p,q,r)) which will take input array, 
with marked indices, (p,q,r) and create copies of the subarray arr[p:q] (both inclusive) and ar[q+1:r]
later it will merge the arrays into the original array arr[p:r] such that over all segment p:r becomes sorted
"""

def mergesort(arr, p , r):
	if p<r:				# The base case
		q = int((p+r)/2);   
		mergesort(arr, p, q);
		mergesort(arr,q+1,r);
		merge(arr,p,q,r)
		
def merge(arr,p,q,r):
	# make subarrays copy 
	#left will contain the elements [p .. q] and right will contain [q+1 .. r] (start index = 1, inclusive)
	#print("arr ="+str(arr[p:r+1]))
	left = arr[p:q+1]  # q+1 because in python list slicing the upper bound is exclusive
	#print("left =" + str(left))
	right = arr[q+1:r+1]  # r+1 because in python list slicing the upper bound is exclusive
	#print("right =" + str(right))
	
	#traverse the source array from p to r, overwriting the existing value with elements coming from left subarray and right subarray
	j = 0
	k = 0
	for i in range(p,r+1):   #r+1 because range generates the numbers excluding the upper bound 
		#print("i=" + str(i))
		#print("j=" + str(j))
		#print("k=" + str(k))
		
		#if k == len(right) and j == len(left):
		#	return
		# if left array index has not reached its end
		if  j != len(left)  and (k == len(right) or left[j] <= right[k]):
			arr[i] = left[j]
			j += 1
		elif k != len(right) and (j == len(left) or left[j] > right[k]):
			arr[i] = right[k]
			k += 1
		else: return

#tarr = [1,2,4,3,10,6,9,7,3,5,8]
tarr = [10,9,8,7,6,5,4,3,2,1]

mergesort(tarr, 0, len(tarr)-1)

print(tarr)		
		