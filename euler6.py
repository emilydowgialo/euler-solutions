def sums(y):
	total = 0
	for x in range(0,y):
		#x = x**2
		total = total + x**2
		print "x:", x
	return total 

def squareOfSums(y):
	total2 = 0
	for n in range(0,y):
		total2 = total2 + n
		print "n:", n
	return total2**2

y = 101
answer = squareOfSums(y) - sums(y)
print answer
 
