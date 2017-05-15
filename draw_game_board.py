# Print a game board of size NxN 
# Eg
#  --- ---
# |   |   |
#  --- ---
# |   |   |
#  --- ---
def printBoard(size):

	print " --- " * size

	for i in range(0,size):

		print "|    " * (size-1) + "|   |"
		print " --- " * size


def main():

	print "Please enter what size game board you want"
	size = int(raw_input())
	printBoard(size)


if __name__ == '__main__':
	main()