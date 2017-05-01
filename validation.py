class Validation():

	# Ensuring that the data entered is a number
	def isNumber(self, num):

			try:
				# Try to convert value passed to function to an int
				num = int(num)
				return num
			except Exception, e:
				
				print "Please enter a valid number"
				return "x"

