import pytest

def search(s,slst,size):
	result = -1
	for index in range(0,size):
		if s == slst[index]:
			result = index
	return result

print(search("hell",["hi","hello"],2)) 
