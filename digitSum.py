i = 1
a = b = c = d = e = f = 0

while True:
	if i < 10:
		a = a + i
	elif i == 10:
		a = a + 1
 	else:
		b = (i - (i % 10)) / 10
		c = i % 10
		d = b + c
		e = e + d
	i = i + 1
	f = a + e
	if ((i-1)* 10) == f:
		print("Total Sum For ", (i-1), " is: ", f)
		break
