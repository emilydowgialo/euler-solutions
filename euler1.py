def threeOrFive(y):
	total = 0
	for x in range(0,y):
		if x%3 == 0 or x%5 == 0:
			total = total + x
			print "x:", x
	print total 

answer = threeOrFive(1000)
print answer


