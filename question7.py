#a.

def foo(s):
	d = {}
	for ch in s:
		v = d.get(ch,0)
		d[ch] = v + 1
	return d

print(foo('sassafras'))

#b. skip

#c. skip

#d. skip