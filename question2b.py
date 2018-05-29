from question2a import search

def readData():
	temp = input()
	data = temp.split()
	return data
def getGrade(name,data):
	size = len(data)
	return data[search(name,data,size)+1]

finished = False
data = readData()
name = input("Enter a name: ")
terminate = 'XXX'
while not finished:
	grade = getGrade(name,data)
	print(grade)
	name = input("Enter a name: ")
	if name == terminate:
		finished == True
print("Good bye.")


