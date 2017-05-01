class Validation():

	# Ensuring that the data entered is a number
	def isNumber(self, num):

			try:
				# Try to convert value passed to function to an int
				num = int(num)
				return num
			except Exception, e:
				
				print "Please enter a valid number"
				return False

	# Ensure that a positive number is entered
	def isPosNum(self, num):

		num = self.isNumber( num)

		if (num >= 0 ):
			
			return num
		elif (num == False):
			
			return num
		else:

			print "Number is not positive"
			return False
			


