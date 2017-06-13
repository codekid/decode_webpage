# Retrieve the birthday of a user from the dic

def main():

	birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'
    }

	# Print the names(keys) of the persons in the dict
	print "We know the names of: "  
	for names in birthday_list.keys():
		print names
	
	print "Whose birthday do you want to find out?"
	name = raw_input()
	
	print birthday_list[name]


if __name__ == '__main__':
	main()