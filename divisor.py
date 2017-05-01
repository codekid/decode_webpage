from validation import Validation # Custom class

def main():

	validator = Validation()

	# Collect data from user and check if number is positive
	print "Please enter a number"
	num = raw_input()
	num = validator.isPosNum(num)

	# will store all the multiples of the number the user entered
	multiples = []

	
	if num > 0:
		numList = range(1,num+1)

		for i in numList:

			if ((num % i) == 0):
				
				multiples.append(i)
		print "you entered the number " + str(num)
		print "Multiples of "+ str(num) + " are: " + str(multiples)


if __name__ == "__main__":
	main()