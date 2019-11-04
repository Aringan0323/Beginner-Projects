#Adam Ring
#Cosi 10a, Fall 2019
#Programming assignment #5
#
#This program takes in three dates: the 
#current date, and two birthdays. The
#program then returns the number of days
#until each birthday and tells the user
#which birthday is coming sooner.
def convert(m):
#this function converts the month into
#the days since the first day of the
#year
	m = m.lower()
#converts string containing the month into 
#all lowercase characters
	Jan = 0
	Feb = Jan + 31
	Mar = Feb + 28
	Apr = Mar + 31
	May = Apr + 30
	Jun = May + 31
	Jul = Jun + 30
	Aug = Jul + 31
	Sep = Aug + 31
	Oct = Sep + 30
	Nov = Oct + 31
	Dec = Nov + 30
#this table assigns a number of days since
#the first day of the year to the month
#inputed
	if m == "january":
		m = Jan
	elif m == "febuary":
		m = Feb
	elif m == "march":
		m = Mar
	elif m == "april":
		m = Apr
	elif m == "may":
		m = May
	elif m == "june":
		m = Jun
	elif m == "july":
		m = Jul
	elif m == "august":
		m = Aug
	elif m == "september":
		m = Sep
	elif m == "october":
		m = Oct
	elif m == "november":
		m = Nov
	elif m == "december":
		m = Dec
#this if/elif statement assigns a number to 
#the month inputted
	return(m)


def countdown(x, y):
#this function calculates the number of days
#from the first date inputted "x", to the 
#second date inputted "y".
	if x > y:
		remainder = x - y
	elif x < y:
		remainder = 365 - (y - x)
	else:
		remainder = 0

	return(remainder)


def birthday():
	
	
	todmon = str(input("Enter today's month:"))
	
	todmon_int = convert(todmon)

	today = int(input("Enter today's day:"))
	
	currdate = (today + todmon_int)
#currdate is a number that is the days since
#the first day of the year of the current 
#date inputted
	mon1 = input("Enter the month of the first birthday:")
	
	mon1_int = convert(mon1)

	day1 = int(input("Enter the day of the first birthday:"))

	bday1 = (day1 + mon1_int)
#bday1 is the number that is the days since
#the first day of the year of the first
#birthday inputted. The same principle applies
#to bday2
	mon2 = input("Enter the month of the second birthday:")

	mon2_int = convert(mon2)

	day2 = int(input("Enter the day of the second birthday:"))

	bday2 = (day2 + mon2_int)

	days_left1 = countdown(bday1, currdate)
#applies the countdown function to the 
#first birthday and the current date, assigning
#the variable "days_left1" to the number of 
#days in-between the first birthday
#and the current date. The same applies for 
#the assignment below.
	days_left2 = countdown(bday2, currdate)

	print("There are ", days_left1, " days left until the first birthday.")
	print("There are ", days_left2, " days left until the second birthday.")
	if days_left1 > days_left2:
		print("The second birthday is coming sooner than the first birthday.")
	elif days_left2 > days_left1:
		print("The first birthday is coming sooner than the second birthday.")
	else:
		print("Both birthdays are on the same day.")
#prints everything

birthday()