def listfunc(lst):
	size = len(lst)
	result = None
	for i in range(0,size):
		if lst[i] < 0:
			result = lst[i]
	return result

lst = [1,4,5,3,4]
print(listfunc(lst))
