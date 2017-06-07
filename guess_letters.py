#import pudb; pudb.set_trace()
# Play a game of Hangman, User tries to guess the word.
# If he/she guesses correctly then the correct letter is printed out along with the remaining blank spaces
# Eg.
# E _ A _ _ _ A T E

correctLetters = []

# Search if the letter that was entered by the user is in the word
def searchLetter(word, letterChoice):

	global correctLetters
	beginSearch = 0

	# Search for letter. If word is not found then the function returns -1
	letterIndex = word.find(letterChoice,beginSearch)
	if letterIndex == -1:
		print "Incorrect!"

	while (letterIndex != -1):
		
		# If we haven't already added this letter to the list of correct letters then add it
		# Shift start point of search by 1 position
		if letterIndex not in correctLetters:
			
			correctLetters.append(letterIndex)
			beginSearch = letterIndex + 1
		else:
			letterIndex = -1

		letterIndex = word.find(letterChoice,beginSearch)


# Print out the word
def printLetters(word):

	global correctLetters
	unfinishedWord=""

	for index, letter in enumerate(word):
		
		# Use the index of the letter to check if the user guessed correctly
		if index in correctLetters:
			unfinishedWord = unfinishedWord + letter + " "
		else:
			unfinishedWord = unfinishedWord + "_ "

	return unfinishedWord

# Check if the user guessed the entire word
def isFinished(unfinishedWord):

	c="_"
	if c in unfinishedWord:
		return False
	else:
		return True

def main():

	global correctLetters

	word = "EVAPORATE"
	wordLength = len(word)
	unfinishedWord =""
	done = False
	guessedLetters = []

	print "Welcome to Hangman!"
	print "_ " * wordLength

	while (done == False):

		letterChoice = str.upper(raw_input())
		if letterChoice in guessedLetters:
			print "You already guessed the letter " + letterChoice
		else:

			guessedLetters.append(letterChoice)
			searchLetter(word, letterChoice)
			# print correctLetters
			unfinishedWord = printLetters(word)
			done = isFinished(unfinishedWord)

		print unfinishedWord

	print "Congrats!! You solved the word!!"
		
if __name__ == "__main__":
	main()