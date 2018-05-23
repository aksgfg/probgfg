"""

"""
# sum of elements of an array recursive

def sumarr(lst):
	#leng = len(lst)
	#last = lst[len(lst)-1]
	
	if len(lst) == 1:
		return lst[0]
	elif len(lst) == 0:
		return 0
	else: 
		#print (str(lst[-1]) + "+")
		return lst[-1] + sumarr(lst[:-1])
	
#l = [1,2,3,4,5,6,7,8,9,10]
t=int(input())
for i in range(0,t):
	n=int(input())
	s = sumarr(list(map(int,input().split())))
	#print("sum"+str(l)+"="+str(s))
	print(str(s))


