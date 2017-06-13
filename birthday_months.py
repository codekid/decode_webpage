import json
from collections import Counter

def summarizeMonths(birthdays):

	pass

def main():

	months = {
		1: "January",
		2: "February",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10:"October",
		11:"November",
		12:"December"
	}

	filename = "birthdays.json"
	birth_months = []

	with open(filename, "r") as f:
		birthdays = json.load(f)

	print birthdays

	for person, dob in birthdays.iteritems():
		
		# split the date of birth of each entry. Check the month in the months dict and add to birth_months list 
		dob = dob.split("/")
		birth_months.append( months[ int( dob[0] ) ] ) 

	# Counter used to summarize the number of months
	c = Counter(birth_months)
	print c

	# print birth_months

if __name__ == "__main__":
	main()