from validation import Validation	# Custom class


def main():

	validator = Validation()
	while True:

		print "Pick a number, any number."		
		num = raw_input()

		# validate if a number was entered. Otherwise return x
		num = validator.isNumber(num)
	
		if (num != False):
			break
		
	
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b =[]
	lt_five = []

	# loop through the list a 
	# create a new list with all numbers less than num
	# create another list with all numbers less 5
	for number in a:

		if (number < num):
			b.append(number)

		if (number < 5):
			lt_five.append(number)

	# Print the list and number entered. 
	# Results are converted to string
	print "numbers less than " + str(num) + ": " + str(b) 
	# msg = '{header}{lst}'.format(header=num, lst=b)
	print "numbers less than 5 in the entire list: " + str(lt_five)

if __name__ == "__main__":
	main()