import math

y = 600851475143
x = int(math.sqrt(y))

def notPrime(test):
	sqrt = int(math.sqrt(test))
	for n in range (2,sqrt+1):
		if test%n == 0:
			return True
	# now we are done with the loop
	return False

print "notPrime(5) should be False", notPrime(5)
print "notPrime(100) should be True", notPrime(100)

for n in range (2,x+1):
	#print n, y%n, notPrime(n)
	if y%n == 0 and notPrime(n) == False:
		# n is a prime factor
		print n








	