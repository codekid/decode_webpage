# Retrieve the birthday of a user from the dic
import json
import os

# Print all names
def printNames(birthdays):

	# Print the names(keys) of the persons in the dict
	print "We know the names of: "  
	for names in birthdays.keys():
		print names

# Find the birthday of user
def findBirthday(birthdays):

	printNames(birthdays)
	print "Whose birthday do you want to find out?"
	name = str(raw_input())

	# Return true or false if key(Name of person) is in the dictionary
	isFound = name in birthdays
	print isFound

	if ( isFound == True):
		print "The birthday of " + name + " is " + birthdays[name]
	else:
		print name + " has not been found. Please try another name"

# Add a new Person 
def addBirthday(birthdays):

	print "What's the user's name?"
	name= raw_input()
	print "When's their birthday?"
	dob= raw_input()

	# Add new person to json file
	birthdays[name]=dob
	return birthdays

# Save data to file
def writeToFile(birthdays, filename):
	
	with open(filename, "w") as f:
		json.dump(birthdays, f)



def main():

	filename ="birthdays.json"

	if os.path.isfile(filename) == False:

		print "File does not exist as yet, creating variable"
		birthdays = {
			'Albert Einstein': '03/14/1879',
			'Benjamin Franklin': '01/17/1706',
			'Ada Lovelace': '12/10/1815',
			'Donald Trump': '06/14/1946',
			'Rowan Atkinson': '01/6/1955'
		}
	else:
		
		print "Reading JSON file"
		with open(filename, "r") as f:
			birthdays = json.load(f)


	choice =0
	while choice != 3:
		
		print """	
			Would you like to:
			1. Find someone's birthday
			2. Add a new Person's birthday
			3. Exit
		"""
		choice = int(raw_input())
		if choice == 1:
			findBirthday(birthdays)
		elif choice == 2:
			addBirthday(birthdays)

	print "Saving file..."
	writeToFile(birthdays, filename)
	print "Saved!!"

if __name__ == '__main__':
	main()