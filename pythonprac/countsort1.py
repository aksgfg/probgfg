# count sort from cormen
# it is effective if the elements of array strictly lie in a range [0,k] where k is some integer (not very big)
# there will be 3 arrays used arr[1..n] (input array),  C[0..k] (temporary work array to count frequency of occurance of 0...k in the input array) 
# and finally B[1 .. n] the output array
# The logic is to count no. of elements in the input which is less than or equal to elements in [0 .. k]. These counts will be derived from already populated C[0..k]
# These counts will later be used in generating the final array which will be sorted version of the input array.

def countsort(arr,k):
	c = [0] * (k+1)
	for i in range(0,len(arr)): # this will generate from 0 to len(arr) - 1
		#count the occurance of 0 .. k in input array.
		c[arr[i]] += 1
	print("1st c array")
	print(c)
	#we have the count now. We can iterate and modify c[] again so that now each position contains the updated count of elements <= position value [0..k]
	for j in range(1,k+1): # last index should be k-1;  upper bound in range() is chosen k 
		# because range function generates values from lower bound(inclusive) to upper bound(exclusive) e.g. range(0,5) will generate [0,1,2,3,4]
		#for l in range(0,j):   WRONG
		#	c[j] += c[l] WRONG
		c[j] = c[j] + c[j-1]
	# its end of the loop. Instead of frequency count of [0..k] elements,  c[j] now contains count of all elements in the input which are <= j (lies in [0 .. k]) in value
	print("after c array mod")
	print(c)
	
	#start building the output array 
	b = [0] * len(arr)
	print (len(b))
	
	print (len(c))
	for m in range(0,len(arr)):
		#print("arr[m] =" + str(arr[m]))
		#print("c[arr[m]] =" + str(c[arr[m]]))
		b[c[arr[m]]-1] = arr[m]
		c[arr[m]] -= 1
	return b
	
# driver code 
tarr = [5,7,4,7,9,2,3,1,6,3,8,0,5,3]
b = countsort(tarr,9)  #suggested improvement: instead of explicitly telling k=9. find it out using max 
print(b)
	