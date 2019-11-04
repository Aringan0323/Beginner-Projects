#Adam Ring
#Cosi 10a, Fall 2019
#Programming Assignment #6
#
#Description: This function prompts the user to enter a first and last name
#and then converts this name into piglatin.

def convert(n):
	print(n[1].upper() + n[2:len(n)] + n[0] + "ay ", end="")
	#converts the string "n" into piglatin using string alteration functions.

def piglat(first, last):
	#converts first and last names into piglatin.
	print(convert(first))
	print(convert(last))

def main():
	f = str(input("Please enter your first name:"))
	l = str(input("Please enter your last name:"))
	#promts the user to enter a first and last name.
	piglat(f, l)
	#converts each name into piglatin.

main()