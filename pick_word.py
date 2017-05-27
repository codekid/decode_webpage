# Download the sowpods list of words from the website http://norvig.com/ngrams/sowpods.txt
# Save the list to a file
# Find the total number of words in the file then randomly select a word and print to show the user
import urllib2
from random import randint

fileName = "sowpods.txt"

# Write data to the file
def writeToFile(data):

	global fileName
	f = open(fileName,"w")

	for line in data:

		f.write(line)
	f.close

# Find how many words there are in the file
def getWordCount():

	global fileName
	with open(fileName, "r") as f:
		
		for i, l in enumerate(f):
			pass
	return i

# search for word in the list that matches the line number
def findWord(searchKey):

	global fileName
	with open(fileName, "r") as f:

		for i, l in enumerate(f):

			if(i == searchKey):
				return l


def main():

	global fileName

	# get data from website and write to a file
	urlTarget = "http://norvig.com/ngrams/sowpods.txt"
	data = urllib2.urlopen(urlTarget).read()
	writeToFile(data)

	wordCount = getWordCount()
	print "The " + fileName + " file contains " + str(wordCount) + " words."

	# Randomly pick a line number for a word 
	searchKey = randint(1,wordCount)
	wordChoice = findWord(searchKey)
	print "The word chosen is " + str(wordChoice).strip() + ". This is word number " + str(searchKey) + " in the list."


if __name__ == "__main__":
	main()