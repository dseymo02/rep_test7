def perfect(n):
	sum = 0
	for i in range(1,n):
		if n % i == 0:
			sum += i
	return sum == n

n = 500
for i in range(1,n+1):
	if perfect(i):
		print(i)

