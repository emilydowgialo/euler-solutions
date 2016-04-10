import math

def triplet(test):
	for a in range(1,test):
		for b in range(1,test):
			c = (a**2) + (b**2)
			c = math.sqrt(c)
			if a + b + c == 1000:
				print a,b,c
				return a*b*c

answer = triplet(1000)
print answer



					