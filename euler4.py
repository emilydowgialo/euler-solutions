def palindrome(test):
	largestNumber = 100
	for x in range(100,test):
		for y in range(100,test):
			if str(x * y)[::-1] == str(x * y):
				v = x * y
				if v > largestNumber:
					largestNumber = v
				print x,y
	return largestNumber

answer = palindrome(1000)
print answer
