import math

def notPrime(test):
	sqrt = int(math.sqrt(test))
	for n in range (2,sqrt+1):
		if test%n == 0:
			return True
	# now we are done with the loop
	return False

count = 1
cat = 2
while count<10002:
	if notPrime(cat) == False:
		count = count + 1
		print cat
	cat = cat + 1	
