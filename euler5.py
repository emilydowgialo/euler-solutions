
def multipleOf2thru20(test):
	""" return True if test is a multiple of 2 thru 20
	return False otherwise
	"""
	for y in range(2,21):
		if test % y != 0:
			return False
	return True

test = 20
while multipleOf2thru20(test) == False:
	test = test + 1
print test



