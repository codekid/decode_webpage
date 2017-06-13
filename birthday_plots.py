import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

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

	output_file("months_histogram.html")

	# Initialize x axis, y axis 
	x_categories =[value for x, value in months.iteritems()]
	x = [ month for month in c]
	y = [ value for month, value in c.iteritems()]

	# Prepare the historgram
	p = figure(title="Number of People Born in Each Month", x_range=x_categories, plot_width=800)
	p.vbar(x=x, top=y, width=0.5)

	print x

	show(p)


if __name__ == "__main__":
	main()