# Ask the user from a number between 0 and 100
# Each time the user guesses ask whether the number was too high, too low or guessed correctly
def guessNumber(userGuess):

	numberRange = populateList()

	first = 0
	last = len(numberRange)-1
	found = False
	guessCount = 0

	while first <= last and not found:
		
		# print "First is " + str(first)
		# print "Last is " + str(last)
		print numberRange[first:last]
		guessCount += 1

		# find the midpoint of the list we're working with
		midpoint = (first+last)//2
		# print "Midpoint " + str(midpoint)

		print "Was your number " +str(numberRange[midpoint]) +"?"
		userResponse= raw_input().lower()

		if (userResponse == "yes"):
			print "Awesom I found you number!  and  I only had to guess " + str(guessCount) + " time(s) :-)."
			found = True
		elif ( userResponse == "too high"):
			
			# Mid point - 1 of search range now becomes the last element
			last = midpoint-1
			print "less than"
		elif(userResponse == "too low"):
			
			# Mid point + 1 of search range becomes the first element
			first = midpoint+1
		else:
			if ( userGuess < numberRange[midpoint]):
				last = midpoint-1
				print "less than"
			else:
				first = midpoint+1

	print found
	return found

# Creat a list with numbers from 0 - 100
def populateList():

	myList = []
	for i in range(0,102):
		myList.append(i)

	return myList



		

def main():

	print "Think of a number between 0 and 100 and tell me"
	userGuess = int(raw_input())
	guessNumber(userGuess)

if __name__ == '__main__':
	main()