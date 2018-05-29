#a.

nums = [1,2,-3,4,5,6]
temp = nums[0] + nums[-1]
nums.append(nums[0] + nums[-1])
print(nums)

#b.

for i in nums:
	if i < 0:
		nums.remove(i)
print(nums)

#c.
a = 3
b = 4
c = 3
print("The average is " + str((a+b+c)/3))