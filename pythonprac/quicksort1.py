# quicksort implementation from cormen 

def quicksort(arr,p,r):
	#problem will be solved by calling partitioning procedure recursively. where the size will reduce at each recursion stack. base case size should be 1
	#or we can say when p = r (this only happen when they both become 1). so only when p != r we need to carry on the recursion.
	if p < r:
		#first find the pivot index because that will be used to divide the problem recursively
		q = partition(arr,p,r)
		#element at qth index has already acheived its position in the sorted array and can be left untouched. so to divide the problem 
		#we will leave out qth position element(its not the part of problem anymore) and
		#call with subarrays arr[p .. q-1] and arr[q+1 .. r] (the subarrays left and right side of it)
		quicksort(arr,p,q-1)
		quicksort(arr,q+1,r)

#most important part...
def swap(arr,a,b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

def partition(arr,p,r):
	x = arr[r]  #taking last element as initial pivot
	i=p-1
	for j in range(p,r): #loop from p to r-1
		if arr[j] <= x: #collect whatever element is less than pivot at one side of the arr[p .. r] array
			i=i+1
			swap(arr,i,j)
		#at the end of the loop, all elements smaller than pivot get collected towards the left side of subarray arr[p..r] 
		#i takes the value of the index of last element which is less than or equal to it.
	# loop has finished, pivot is still at the right end of the sub arr, leaving the pivot, the rest of the array is divided into 2 segments, 
	# one segment has all values less than or equal to pivot value, and another segment after the 1st segment has values greater than the pivot element
	# insert the pivot element in between the 1st segment and the second segment. So that the resulting subarray will be
    # of the form "LxR" where L is the subsubarray having values <= pivot value, x is the pivot value, R is the subarray having values > pivot value
	# this is what was supposed to be returned
	swap(arr,i+1,r)
	return i+1

#driver code	
tarr = [10,9,8,7,6,5,4,3,2,1]
quicksort(tarr, 0, len(tarr)-1)
print(tarr)		

	

