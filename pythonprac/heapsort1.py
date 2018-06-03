"""Implementaion of heapsort from CLRV.

Contains functions to access parent, left-child, right-child of a node in the Max-heap,
heapify method to create heap out of an unordered array
if the array index varies from 1 to heap.size, for a given element position i in the heap/array,
left, right and parent node can be obtained as follows:

parent(i):
    return floor(i/2)

left(i):
    return 2i

right(i):
    return 2i+1

but if our array indices varies from 0 to heap.size-1 (0 index array) we can modify the above as
follows

parent(k):
    if k%2 == 0:
        return 1/2*(k-1)
    else:
        return 1/2*(k-2)

left(k):
    return 2k+1

right(k)
    return 2k+2

"""

def left(k):
    """returns the index of left child in the heap representaion of array"""
    
